// Third party
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io"

// Project
import { IStateWithPagination } from "@/utils/types"

interface IPageProps {
  data: IStateWithPagination<any> | undefined
}

export const Pagination = ({ data }: IPageProps) => {

  if (!data?.results.length || data === undefined)
    return null

  return (
    <div className="flex items-center justify-end gap-4">
      <button
        disabled={!data.previous}
        className="outline-none flex items-center p-2 select-none rounded-lg border border-purple-800 font-sans text-xs font-medium uppercase text-purple-800 transition-all hover:opacity-75 focus:ring focus:ring-gray-300 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-70 disabled:shadow-none"
        type="button">

        <span className="flex items-center gap-2">
          <IoIosArrowBack size={20} />
        </span>
      </button>

      <p className="flex gap-2 font-sans text-base antialiased font-normal leading-relaxed text-gray-500">
        <span>Página</span>
        <strong className="text-purple-700">{data.current_page || '---'}</strong>
        <span>De</span>
        <strong className="text-purple-700">{data.page_count || '---'}</strong>
      </p>

      <button
        disabled={!data.next}
        className="flex items-center p-2 select-none rounded-lg border border-purple-800 text-center align-middle font-sans text-xs font-medium uppercase text-purple-800 transition-all hover:opacity-75 focus:ring focus:ring-gray-300 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-70 disabled:shadow-none"
        type="button">

        <span className="flex items-center gap-2 w-auto">
          <IoIosArrowForward size={20} />
        </span>
      </button>
    </div>
  )
}