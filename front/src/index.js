import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Main from "./Main/Main";
import Blog from "./Blog/Blog";
import Account from "./Account/Account";
import Header from "./Header";
import Footer from "./Footer";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <Header />
    <h1>Project Zero</h1>
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/blog/" element={<Blog />} />
      <Route path="/account/" element={<Account />} />
    </Routes>
    <Footer />
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
