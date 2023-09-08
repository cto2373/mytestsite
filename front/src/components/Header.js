const Header = ({ children }) => {
  return (
    <header className="justify-between flex pr-8 bg-slate-900 text-white">
      <h1 className="   text-6xl"><a href="/">{children}</a></h1>
    </header>
  );
};

export default Header;