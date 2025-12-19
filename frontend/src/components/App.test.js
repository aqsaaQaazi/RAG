// Basic test to verify the testing configuration is working
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '@site/src/components/App';

describe('App Component', () => {
  test('renders without crashing', () => {
    render(<App />);
    expect(screen.getByText(/Welcome to my App/i)).toBeInTheDocument();
  });
});