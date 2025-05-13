import matplotlib.pyplot as plt
import seaborn as sn

# Function to calculate percentage
def calculate_percentage(df, count_column):
    total = df[count_column].sum()
    df['Percentage'] = (df[count_column] / total) * 100
    return df

# Function to plot bar chart with percentage labels
def plot_bar_chart_with_percentage(data, category_column, count_column, colors):
    # Calculate the percentage using the provided count column
    data = calculate_percentage(data, count_column)
    
    # Create the horizontal bar plot
    ax = plt.barh(data[category_column], data['Percentage'], color=colors)

    # Remove border (spines) around the plot
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Add percentage labels on bars
    for bar in ax:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2, f"{width:.1f}%",
                 ha='left', va='center', fontsize=12, color='black')

    plt.grid(axis='x', linestyle='-', alpha=0.07)
    plt.tight_layout()

    # Show the plot
    plt.show()

def plot_vertical_bar_chart_with_percentage(data, category_column, count_column, colors):
    # Calculate the percentage using the provided count column
    data = calculate_percentage(data, count_column)
    
    # Create the vertical bar plot
    ax = plt.bar(data[category_column], data['Percentage'], color=colors)

    # Remove borders (spines)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Add percentage labels on top of bars
    for bar in ax:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1, f"{height:.1f}%",
                 ha='center', va='bottom', fontsize=12, color='black')

    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='-', alpha=0.07)
    plt.tight_layout()

    # Show the plot
    plt.show()
