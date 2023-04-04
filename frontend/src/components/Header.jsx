import React, { useState } from "react";
import logo from "../assets/logo.jpg";
import { Link, useLocation } from "react-router-dom";
import { SidebarLink } from ".";
import { RiMenuFoldFill } from "react-icons/ri";

const Header = () => {
  const location = useLocation();
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  return (
    <>
      <header className="fixed top-0 left-0 w-full h-[70px] bg-[#dc7ce3] text-white z-50">
        <div className="h-full flex items-center justify-between max-w-7xl mx-auto px-3">
          {/* logo */}
          <div className="flex items-center gap-2">
            <img src={logo} alt="logo" className="w-12 h-12 rounded-full" />
            <h1 className="font-bold text-2xl md:text-3xl font-[Alkatra]">
              Real Home
            </h1>
          </div>

          {/* nav links */}
          <nav className="hidden lg:inline">
            <ul className="flex items-center gap-8">
              <li className={`link ${location.pathname === "/" && "active"} `}>
                <Link to="/">Home</Link>
              </li>
              <li
                className={`link ${
                  location.pathname === "/contact" && "active"
                } `}
              >
                <Link to="/contact">Contact</Link>
              </li>
              <li
                className={`link ${
                  location.pathname === "/listings" && "active"
                } `}
              >
                <Link to="/listings">Listings</Link>
              </li>
              <li
                className={`link ${
                  location.pathname === "/about" && "active"
                } `}
              >
                <Link to="/about">About</Link>
              </li>
            </ul>
          </nav>

          {/* authentication link */}
          <Link
            to="/register"
            className="px-10 py-2 bg-blue-500 rounded hover:scale-105 font-semibold hidden lg:inline"
          >
            Register
          </Link>

          {/* Menu icon */}
          <RiMenuFoldFill
            className="cursor-pointer text-2xl lg:hidden"
            onClick={() => setIsSidebarOpen((prev) => !prev)}
          />
        </div>
      </header>

      {/* nav and authentication links for small screen devices */}
      <div
        className={`fixed top-[70px] w-[200px] bottom-0 bg-[#dc7ce3] lg:hidden ${
          isSidebarOpen
            ? "left-0 duration-[1s]"
            : "left-[-999px] duration-[1.8s]"
        }`}
      >
        <SidebarLink />
      </div>
    </>
  );
};

export default Header;
