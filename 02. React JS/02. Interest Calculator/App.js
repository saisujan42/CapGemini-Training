import logo from './logo.svg';
import './App.css';
import InterestCalculator from './Components/InterestCalculator';

function App() {
  return (
    <div className="App">
      <img src={logo} className="App-logo" alt="logo" />
      <p> Welcome to React. </p>
      <InterestCalculator/>
    </div>
  );
}

export default App;