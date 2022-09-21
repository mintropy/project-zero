import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <div className="Header">
      <h1>Project Zero</h1>
      <Link to={"/"}>Main</Link>
      <br />
      <Link to={"/blog/"}>Blog</Link>
      <br />
      <Link to={"/account/"}>account</Link>
    </div>
  );
};

export default Header;
