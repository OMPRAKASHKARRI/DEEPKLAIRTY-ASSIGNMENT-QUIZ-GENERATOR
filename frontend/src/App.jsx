import React, { useState } from 'react';
import './App.css';
import TabNavigation from './components/TabNavigation';
import QuizGenerator from './components/QuizGenerator';
import HistoryTable from './components/HistoryTable';

function App() {
  const [activeTab, setActiveTab] = useState('generate');

  return (
    <div className="app">
      <header className="app-header">
  <h1>Wikipedia Quiz Generator</h1>
  <p className="subtitle">Turn Wikipedia articles into smart quizzes</p>
</header>


      <TabNavigation activeTab={activeTab} onTabChange={setActiveTab} />

      <main>
        {activeTab === 'generate' ? <QuizGenerator /> : <HistoryTable />}
      </main>
    </div>
  );
}

export default App;
