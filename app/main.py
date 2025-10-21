"""
Core functionality for the starter science package.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_sample_data(n_points=100, noise_level=0.1, seed=42):
    """
    Generate sample data for demonstration.

    Parameters
    ----------
    n_points : int, default=100
        Number of data points to generate
    noise_level : float, default=0.1
        Standard deviation of noise
    seed : int, default=42
        Random seed for reproducibility

    Returns
    -------
    pd.DataFrame
        DataFrame with columns 'x' and 'y'
    """
    np.random.seed(seed)
    x = np.linspace(0, 10, n_points)
    y = np.sin(x) + noise_level * np.random.randn(n_points)

    data = pd.DataFrame({
        'x': x,
        'y': y
    })

    return data


def plot_data(data, title="Sample Data with Noise", figsize=(10, 6)):
    """
    Create a simple plot of the data.

    Parameters
    ----------
    data : pd.DataFrame
        Data to plot with columns 'x' and 'y'
    title : str, default="Sample Data with Noise"
        Plot title
    figsize : tuple, default=(10, 6)
        Figure size
    """
    plt.figure(figsize=figsize)
    plt.plot(data['x'], data['y'], 'b-', alpha=0.7, label='Data')
    plt.plot(data['x'], np.sin(data['x']), 'r--', label='True function')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
