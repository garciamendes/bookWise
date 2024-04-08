export interface ICategory {
  title: string
  slug: string
}

export interface IFiltersExplore {
  categories?: string[]
  search?: string
  page?: string
}

export interface IBook {
  uid: string
  title: string
  description: string
  author: string
  thumbnail: string
  total_pages: number
  categories: Array<ICategory>
  rating: number
  created: string
}

export interface IStateWithPagination<T> {
  total: number | string,
  page_size: number | string,
  page_count: number | string,
  current_page: number | string,
  next: null | number | string,
  previous: null | number | string,
  results: T
}