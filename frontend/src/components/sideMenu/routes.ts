import { ISideMenuProps } from "./types";
import { PiBinoculars, PiChartLineUpLight } from "react-icons/pi";

export const routes: ISideMenuProps[] = [
  {
    icon: PiBinoculars,
    name: 'Explorar',
    path: '/home'
  },
  {
    icon: PiChartLineUpLight,
    name: 'Início',
    path: '/home/initial'
  }
]