import React, { useState } from "react";

const AuthForm = ({ page }) => {
  const [formInputs, setFormInputs] = useState({
    name: "",
    email: "",
    password: "",
    password2: "",
  });

  const handleInputChange = (e) => {
    setFormInputs({ ...formInputs, [e.target.id]: e.target.value });
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <form onSubmit={handleFormSubmit} className="mt-6 w-full md:w-[350px]">
      {page === "Register" && (
        <input
          type="text"
          placeholder="Name"
          id="name"
          value={formInputs.name}
          onChange={handleInputChange}
          className="input"
        />
      )}

      <input
        type="email"
        placeholder="Email"
        id="email"
        value={formInputs.email}
        onChange={handleInputChange}
        className="input"
      />
      <input
        type="password"
        placeholder="Password"
        id="password"
        value={formInputs.password}
        onChange={handleInputChange}
        className="input"
      />
      {page === "Register" && (
        <input
          type="password"
          placeholder="Confirm Password"
          id="password2"
          value={formInputs.password2}
          onChange={handleInputChange}
          className="input"
        />
      )}

      <button
        type="submit"
        className="w-full py-2 bg-[#432432] rounded text-white mt-2 lg:mt-4 hover:scale-[1.03]"
      >
        {page}
      </button>
    </form>
  );
};

export default AuthForm;
