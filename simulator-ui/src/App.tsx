import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { Button } from '@/components/ui/button';
import { Progress } from "@/components/ui/progress"

function App() {
  const [count, setCount] = useState(0);

  // Event handler for button clicks
  const handleButtonClick = () => {
    setCount((prevCount) => prevCount + 1);
  };

  return (
    <div>
      <Button variant="outline">Button</Button>
      <Progress value={33} />

    </div>
  );
}

export default App;
