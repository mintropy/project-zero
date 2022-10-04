import React from "react";
import { Link } from "react-router-dom";
import "./index.css";

const Header = () => {
  return (
    <div className="Header">
      <Link to={"/"}>Zero</Link>
      <Link to={"/blog/"}>Blog</Link>
      <Link to={"/account/"}>account</Link>
    </div>
  );
};

export default Header;
