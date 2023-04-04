import React from "react";
import authImage from "../assets/img.webp";
import { Link } from "react-router-dom";
import AuthForm from "./AuthForm";

const Auth = () => {
  return (
    // background image
    <div className="mt-[70px] bg-[url('https://i.pinimg.com/originals/21/79/c9/2179c9ee905a18ad079f1b8ae798a68c.jpg')] h-[calc(100vh-70px)] bg-no-repeat bg-cover ">
      <div className="w-full h-full bg-[rgba(29,29,24,0.52)] p-4 md:p-8 lg:px-20 py-8 xl:px-40 ">
        <div className="grid grid-cols-1 lg:grid-cols-2 bg-white w-full h-full rounded-md">
          {/* image container */}
          <div className="hidden lg:inline bg-[#eff5f7] h-full w-full p-4 rounded-md">
            <img src={authImage} alt="authImage" className="h-full" />
          </div>

          {/* form */}
          <div className="h-full w-full p-4 text-center">
            <div className="flex items-center justify-end gap-3">
              <p>Have an account?</p>
              <Link
                to="/login"
                className="bg-[#95d7e633] px-10 hover:scale-105 font-semibold py-2 rounded-3xl"
              >
                Sign In
              </Link>
            </div>
            <h1 className="mt-4 mb-1 font-bold text-xl lg:text-2xl font-[Alkatra]">
              Welcome to Real Home.
            </h1>
            <p>Managing your property has never been easier.</p>
            <AuthForm />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Auth;
