export const BookListSkeleton = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 auto-rows-[160px] my-3">
      {Array.from({ length: 10 }).map((_, index) => {
        return (
          <div key={index} className="flex items-center gap-3 rounded-lg p-2 bg-slate-800">
            <div className="skeleton h-[145px]  w-[140px]"></div>

            <div className="flex flex-1 flex-col h-full justify-between">
              <div className="flex flex-col gap-1">
                <div className="skeleton w-full h-4"></div>
                <div className="skeleton w-full h-4"></div>
              </div>

              <div className="skeleton w-full h-4"></div>
            </div>
          </div>
        )
      })}
    </div>
  )
}