// Third party
import { IconType } from "react-icons"
import { SearchBar } from "../searchBar"

export interface IHeaderProps {
  name: string
  icon: IconType
  hasSearchBar?: boolean
  nameSearch?: string,
  placeholder?: string
}

export const Header = ({ name, icon: Icon, hasSearchBar = false, nameSearch, placeholder = '' }: IHeaderProps) => {
  return (
    <header className="flex items-center justify-between w-full">
      <div className="flex items-center gap-3">
        <Icon size={25} className="text-slate-300" />
        <strong className="text-base">{name}</strong>
      </div>

      {hasSearchBar && (
        <SearchBar name={nameSearch} placeholder={placeholder} />
      )}
    </header>
  )
}