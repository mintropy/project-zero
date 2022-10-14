import { BrowserRouter, Route, Routes } from "react-router-dom";
import Main from "./Main/Main";
import Blog from "./Blog/Blog";
import Account from "./Account/Account";
import Header from "./Header";
import Footer from "./Footer";
import React, { useState } from "react";

const App = () => {
  const [isLogin, setIsLogin] = useState(false);

  const toggleLogin = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route
            path="/"
            element={<Main isLogin={isLogin} toggleLogin={toggleLogin} />}
          />
          <Route path="/blog/" element={<Blog />} />
          <Route path="/account/" element={<Account />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
};

export default App;
