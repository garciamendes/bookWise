'use client'

// React
import { useEffect, useState } from "react"
import { usePathname, useSearchParams, useRouter } from "next/navigation"

// Third party
import { dataTagSymbol, useQuery } from "@tanstack/react-query"
import { PiBinoculars } from "react-icons/pi"
import { AxiosResponse } from "axios"
import { toast } from "sonner"
import { BiLoaderAlt } from "react-icons/bi"

// Project
import { api } from "@/services/api"
import { Header } from "@/components/header"
import { IBook, ICategory, IFiltersExplore, IStateWithPagination } from "@/utils/types"
import { Pagination } from "@/components/pagination"
import Image from "next/image"
import { Star } from "@/components/stars"
import { BookListSkeleton } from "@/components/loaders-skeletons/bookListSkeleton"

const Home = () => {
  const searchParams = useSearchParams()
  const router = useRouter()
  const pathname = usePathname()

  const params = new URLSearchParams(searchParams.toString())

  const { data: listCategories, isError, isFetching } = useQuery<ICategory[]>({
    queryKey: ['categories'],
    queryFn: async () => {
      const response: AxiosResponse<ICategory[]> = await api.get('/api/categories/categories-filters/')

      if (!params.get('categories') || params.get('categories') === 'all') {
        setFilters(prevState => ({
          ...prevState,
          'categories': ['all']
        }))
      } else {
        setFilters(prevState => ({
          ...prevState,
          'categories': params.get('categories')?.split(',')
        }))
      }

      return response.data
    },
  })

  const {
    data: listBooks,
    isError: isErrorListBooks,
    isFetching: isLoadingListBooks,
    refetch: refetchListBooks } = useQuery<IStateWithPagination<Array<IBook>>>({
      queryKey: ['books'],
      queryFn: async () => {
        const response = await api.get(`/api/book/?${params.toString()}`)

        return response.data
      }
    })

  const [filters, setFilters] = useState<IFiltersExplore>({})

  useEffect(() => {
    if (!isError)
      return

    toast.error('Erro ao tentar carregar as categorias')
  }, [isError])

  useEffect(() => {
    if (!isErrorListBooks)
      return

    toast.error('Erro ao tentar carregar a lista de livros')
  }, [isErrorListBooks])

  useEffect(() => {
    setFilters(prevState => ({
      ...prevState,
      'search': params.get('search') as string,
      'page': params.get('page') as string
    }))
  }, [params.get('search'), params.get('categories'), params.get('page')])

  useEffect(() => {
    const { categories } = filters
    const categorieToFilter = categories?.join(',')

    params.set('categories', categorieToFilter as string)
    router.push(`${pathname}?${params.toString()}`)
    refetchListBooks()
  }, [filters.categories, filters.search, filters.page])

  const handleSendFilterCategories = (slug: string) => {
    if (filters.categories?.includes(slug)) {
      const newArray = filters.categories.filter(category => category !== slug)
      setFilters(prevState => ({
        ...prevState,
        'categories': newArray
      }))
    } else {
      if (slug === 'all') {
        const newArray = [] as string[]

        newArray?.push(slug)
        setFilters(prevState => ({
          ...prevState,
          'categories': newArray
        }))

        return
      }

      const newArray = filters.categories?.filter(category => category !== 'all')

      newArray?.push(slug)
      setFilters(prevState => ({
        ...prevState,
        'categories': newArray
      }))

    }
  }

  const renderPagination = () => {
    return <Pagination data={listBooks} />
  }

  const renderContent = () => {
    if (isLoadingListBooks) {
      return (
        <BookListSkeleton />
      )
    }


    if (!listBooks?.results.length) {
      return (
        <div className="flex flex-col text-center w-full justify-center items-center">
          <strong className="text-base text-white">Nenhum livro encontrado!</strong>
          <span className="text-sm text-white">verifique os filtros aplicados</span>
        </div>
      )
    }

    return (
      <>
        {renderPagination()}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 auto-rows-[160px] my-3">
          {listBooks?.results.map(book => {
            return (
              <div className="flex items-center gap-3 rounded-lg p-2 bg-slate-800">
                <div className="h-[145px]">
                  <img
                    className="h-full w-[140px] object-cover rounded-lg"
                    src='https://images.unsplash.com/photo-1561312176-5aedf7172115?q=80&w=1972&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' alt='capa livro' />
                </div>

                <div className="flex flex-1 flex-col h-full justify-between">
                  <div className="flex flex-col gap-1">
                    <strong>{book.title || '---'}</strong>
                    <span className="text-slate-500">{book.author || '---'}</span>
                  </div>

                  <Star.Root rating={book.rating} />
                </div>
              </div>
            )
          })}
        </div>

        {renderPagination()}
      </>
    )
  }

  return (
    <div className="flex flex-col h-full w-full">
      <Header name="Explorar" icon={PiBinoculars} hasSearchBar placeholder="Buscar livro ou autor" />

      <div className="w-full overflow-auto">
        <div className="flex flex-1 items-center gap-3 mt-3">
          {isFetching ? (
            <span className="w-full flex justify-center items-center py-5">
              <span className="loading loading-dots loading-xs"></span>
            </span>
          ) : (
            <>
              <button
                onClick={() => handleSendFilterCategories('all')}
                className={`cursor-pointer border rounded-full border-purple-900 px-3 py-1 hover:bg-purple-900 hover:text-white duration-300 ${filters.categories?.includes('all') && 'bg-purple-900 text-white'}`}>
                Tudo
              </button>

              {listCategories?.map(category => (
                <button
                  onClick={() => handleSendFilterCategories(category.slug)}
                  className={`cursor-pointer border rounded-full border-purple-900 px-3 py-1 hover:bg-purple-900 hover:text-white duration-300 ${filters.categories?.includes(category.slug) && 'bg-purple-900 text-white'}`}>
                  {category.title || '---'}
                </button>
              ))}
            </>
          )}
        </div>
      </div>

      <div className="flex flex-col mt-4 flex-1 overflow-auto">
        {renderContent()}
      </div>
    </div>
  )
}

export default Home