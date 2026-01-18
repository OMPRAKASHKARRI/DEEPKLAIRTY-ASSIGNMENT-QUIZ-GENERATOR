import React from 'react';

const TabNavigation = ({ activeTab, onTabChange }) => {
    return (
        <div className="tabs">
  <button
    className={activeTab === 'generate' ? 'active' : ''}
    onClick={() => onTabChange('generate')}
  >
    Generate Quiz
  </button>

  <button
    className={activeTab === 'history' ? 'active' : ''}
    onClick={() => onTabChange('history')}
  >
    Past Quizzes
  </button>
</div>

    );
};

export default TabNavigation;
