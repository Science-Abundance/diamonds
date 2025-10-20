#!/usr/bin/env python3
"""
Main script for the starter science project.
Demonstrates basic scientific computing functionality.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_sample_data():
    """Generate sample data for demonstration."""
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + 0.1 * np.random.randn(100)

    data = pd.DataFrame({
        'x': x,
        'y': y
    })

    return data


def plot_data(data):
    """Create a simple plot of the data."""
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'], 'b-', alpha=0.7, label='Data')
    plt.plot(data['x'], np.sin(data['x']), 'r--', label='True function')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sample Data with Noise')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def main():
    """Main function."""
    print("Starting Starter Science Demo...")

    # Generate sample data
    data = generate_sample_data()
    print(f"Generated {len(data)} data points")

    # Basic statistics
    print(f"Mean Y: {data['y'].mean():.3f}")
    print(f"Std Y: {data['y'].std():.3f}")

    # Create plot
    plot_data(data)

    print("Demo completed!")


if __name__ == "__main__":
    main()
