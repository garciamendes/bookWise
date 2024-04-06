// React
import { IconType } from "react-icons"

export interface ISideMenuProps {
  name: string
  icon: IconType
  path: string
  active?: boolean
}