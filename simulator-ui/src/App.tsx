import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { Button } from '@/components/ui/button';
import { Progress } from "@/components/ui/progress"

function App() {
  return (
    <div>
      <Button variant="outline">Button</Button>
      <Progress value={33} />
    </div>
  );
}

export default App;
