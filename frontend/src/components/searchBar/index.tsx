'use client'

// React
import { useCallback, useEffect, useState } from "react"
import { useSearchParams, usePathname, useRouter } from "next/navigation"

// Third party
import { CiSearch } from "react-icons/ci"

export interface ISearchProps {
  placeholder: string
  name?: string
}

export const SearchBar = ({ placeholder, name = 'search' }: ISearchProps) => {
  // States
  const [search, setSearch] = useState('')

  // Hooks
  const searchParams = useSearchParams()
  const pathname = usePathname()
  const router = useRouter()

  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams.toString())
      params.set(name, value)

      return params.toString()
    },
    [searchParams]
  )

  const searchForm = (formData: FormData) => {
    const search = formData.get('search')

    const resultsParams = createQueryString('search', search as string)

    setSearch(search as string)
    router.push(`${pathname}?${resultsParams}`)
  }

  return (
    <form action={searchForm} className="flex items-center border border-purple-900 h-11 w-2/6 px-2 rounded-md">
      <input
        name={name}
        type="text"
        className="bg-transparent h-full w-full outline-none text-gray-400"
        placeholder={placeholder} />

      <button type="submit">
        <CiSearch className="text-purple-400 ml-2 cursor-pointer" size={20} />
      </button>
    </form>
  )
}