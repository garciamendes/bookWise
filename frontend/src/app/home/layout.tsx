'use client'

// React
import React from "react";
import Image from "next/image";
import Link from "next/link";

// Third party
import { PiSignIn } from "react-icons/pi";

// Project
import LogoImg from '@/assets/logo.svg'
import { SideMenu } from "@/components/sideMenu";

const HomeLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex h-full w-full p-4">
      <div className="relative flex flex-col p-3 items-center h-full w-[240px] rounded-xl bg-gray-800 mr-10">
        <Image src={LogoImg} alt='Logo' />

        <SideMenu />

        <Link className='absolute bottom-4 flex items-center gap-4 text-base text-gray-400 hover:text-slate-50' href='/login'>
          <span>Fazer login</span>
          <PiSignIn size={20} className="text-green-100" />
        </Link>
      </div>

      <div className='flex flex-1'>
        {children}
      </div>
    </div>
  )
}

export default HomeLayout
