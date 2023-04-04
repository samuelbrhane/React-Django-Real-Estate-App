import React from "react";

const NotFound = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh]">
      <h1 className="font-bold text-red-400 text-2xl md:text-3xl lg:text-4xl mb-2">
        404 Page Not Found
      </h1>
      <p className="text-semibold text-xl">
        The page you request does not found in this website.
      </p>
    </div>
  );
};

export default NotFound;
