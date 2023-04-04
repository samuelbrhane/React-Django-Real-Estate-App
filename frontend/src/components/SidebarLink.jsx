import React from "react";
import { Link, useLocation } from "react-router-dom";

const SidebarLink = () => {
  const location = useLocation();

  return (
    <section className="flex flex-col justify-between items-center h-full py-4 text-black">
      {/* nav links */}
      <nav>
        <ul className="flex items-center flex-col gap-8">
          <li className={`link ${location.pathname === "/" && "active"} `}>
            <Link to="/">Home</Link>
          </li>
          <li
            className={`link ${location.pathname === "/contact" && "active"} `}
          >
            <Link to="/contact">Contact</Link>
          </li>
          <li
            className={`link ${location.pathname === "/listings" && "active"} `}
          >
            <Link to="/listings">Listings</Link>
          </li>
          <li className={`link ${location.pathname === "/about" && "active"} `}>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>

      {/* authentication link */}
      <Link
        to="/register"
        className="px-10 py-2 bg-blue-500 rounded hover:scale-105 font-semibold text-white"
      >
        Register
      </Link>
    </section>
  );
};

export default SidebarLink;
