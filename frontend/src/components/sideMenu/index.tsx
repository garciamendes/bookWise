'use client'

// React
import Link from "next/link"
import { usePathname } from 'next/navigation'

// Third party
import { pathToRegexp } from 'path-to-regexp'

// Local
import { routes } from "./routes"
import { ISideMenuProps } from "./types"


const SideMenuItem = ({ name, icon: Icon, path, active }: ISideMenuProps) => {
  return (
    <Link className={`flex items-center gap-4 text-base text-gray-400 group-hover:text-slate-50 ${active && 'text-slate-50'} duration-600`} href={path}>
      <Icon size={25} />
      <span>{name}</span>
    </Link>
  )
}

export const SideMenu = () => {
  const router = usePathname()

  const isRouteActive = (pattern: string) => {
    const match = pathToRegexp(pattern).exec(router)
    return !!match
  }

  return (
    <ul className="flex flex-col mt-10 gap-5">
      {routes.map((route, index) => {


        return (
          <li key={index} className="flex relative group duration-600">
            <span className={`absolute duration-300 h-full w-[4px] rounded-lg -left-3 bg-gradient-to-b from-teal-300 to-blue-700 opacity-0 group-hover:opacity-100 ${isRouteActive(route.path) && 'opacity-100'}`}></span>

            <SideMenuItem
              active={isRouteActive(route.path)}
              icon={route.icon}
              name={route.name}
              path={route.path} />
          </li>
        )
      })}
    </ul>
  )
}