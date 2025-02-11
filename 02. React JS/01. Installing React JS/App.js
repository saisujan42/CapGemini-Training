import logo from './logo.svg';
import './App.css';
import Header from './Components/Header';
import Body from './Components/Body';
import Footer from './Components/Footer';

function App() {
  return (
    <div className="App">
      <Header/>
      <img src={logo} className="App-logo" alt="logo" />
      <p> Welcome to React. </p>
      <Body/>
      <Footer/>
    </div>
  );
}

export default App;