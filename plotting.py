import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
"""
go is the main module for creating figures in plotly.
make_subplots is used to create a figure with multiple subplots.
"""
def create_interative_chart(df:pd.DataFrame, title: str="Interactive Chart", indicators =list)->go.Figure:
    """
    Create an interactive chart with multiple indicators.
    Indicators are selected from the DataFrame columns.
    The chart will have a separate subplot for each indicator.
    Parameters:
    - df: DataFrame containing the data to plot.
    - title: Title of the chart.
    - indicators: List of indicators to plot.
    
    Returns:
    - A Plotly Figure object.
    """
    fig = make_subplots(
        rows=3, cols=1, shared_xaxes=True, 
        vertical_spacing=0.05,
        subplot_titles=('CandleStick Chart', 'Volume' ,'Indicators'),
        row_heights=[0.6, 0.2, 0.2]
        )
    """
    Create a 3 layer subplot with shared x-axis.
    The first layer is for the candlestick chart, the second for volume, and the third for indicators.

    CandleStick is a visual representation of price movements with the help of open, high, low, and close prices of the stock.
    They encode data in a way that allows traders to see the patterns and trends in the stock price.
    Volume is the number of shares traded during a specific period.
    Indicators are technical indicators like moving averages, RSI, etc.
    """
    
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['Open'],high=df['High'],
            low=df['Low'],close=df['Close'],
            name='Candlestick',
        ),
        row=1,col=1
    )
    """
    trace means a single plot in the figure.
    Here we are adding a candlestick trace to the first subplot.
    candlestick is a type of financial chart that represents the open, high, low, and close prices of a stock.(OHLC)
    add another data visualization to the figure.
    
    x=df.index means the x-axis will be the index of the DataFrame, which is usually the date.
    open, high, low, close are the columns in the DataFrame that contain the respective prices.
    name='Candlestick' is the name of the trace that will be displayed in the legend.
    """
    overly_indicators = ["SMA", "EMA", "WMA", "BB_Upper", "BB_Lower", "BB_Mid"]
    for ind in set(overly_indicators) & set(indicators):
        if ind in df.columns:
            if ind.startswith("BB_"):
                fig.add_trace(
                    go.Scatter(
                        x=df.index,
                        y=df[ind],
                        name=ind,
                        mode='lines',
                        fill='tonexty',
                        fillcolor='rgba(173, 216, 230, 0.5)',
                        line=dict(width=1.5)
                    ),
                    row=1, col=1
                )
            else:
                fig.add_trace(
                    go.Scatter(
                        x=df.index,
                        y=df[ind],
                        name=ind,
                        mode='lines'
                    ),
                    row=1, col=1
                )
    """
    overly indicatos is a list of indicators that are plotted on the candlestick chart.
    they are only allowd in the price panel.
    the set(overly_indicators) & set(indicators) checks if the indicators are in the DataFrame.
    intersection between allowed overlays and the user-selected indicators.
    if the indicator starts with "BB_", it is plotted as a scatter plot with lines.
    otherwise, it is plotted as a scatter plot without lines.
    fill is done in order to seperate the area between the lines.
    fillcolor='rgba(173, 216, 230, 0.5)' sets the color of the fill to a semi-transparent light blue.
    line=dict(width=1.5) sets the width of the lines to 1.
    """

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df['Volume'],
            name='Volume',
            marker_color='rgba(0, 0, 255, 0.5)',
            showlegend=False
        ),
        row=2, col=1
    )
    """
    Add a bar trace for volume to the second subplot.
    go.Bar creates a bar chart.
    x=df.index means the x-axis will be the index of the DataFrame, which is usually the date.
    y=df['Volume'] means the y-axis will be the volume of shares traded.
    name='Volume' is the name of the trace that will be displayed in the legend.
    marker_color='rgba(0, 0, 255, 0.5)' sets the color of the bars to a semi-transparent blue.
    showlegend=False means we don't want to show the legend for this trace.
    """

    # scatter appears above and the bar plot appears below the scatter plot hence the row=1 and row=2 for bar plot.

    subplot_indicators = ["RSI", "MACD", "MACD_Signal", "MACD_Hist", "Stoch_K", "Stoch_D", "ATR", "OBV", "CMF"]
    for ind in set(subplot_indicators) & set(indicators):
        if ind in df.columns:
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df[ind],
                    name=ind,
                    mode='lines',
                    line=dict(width=1.5, color='rgba(255, 0, 0, 0.7 )')  # Semi-transparent red
                ),
                row=3, col=1
            )
        else:
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df[ind],
                    name=ind
                ),
                row=3, col=1
            )
    """
    subplot_indicators is a list of indicators that are plotted in the third subplot.
    they are only allowed in the indicator panel.
    The difference between subplot and overlay indicators is that subplot indicators are plotted in a seperate panel below the price chart
    and overlay indicators are plotted on the price chrat like moving averages, Bollinger Bands, etc.
    subplot indicators generally reperesent metrics on different scales from the price chart.
    """
    fig.update_layout(
        heigh=800,
        title_text="Stock Chart with Technical Indicators",
        xaxis_rangeslider_visible=False,
        showlegend=True,
    )
    fig.update_xaxes(title_text="Date",row=3,col=1)
    fig.update_xaxes(title_text="Price",row=1,col=1)
    fig.update_xaxes(title_text="Volume",row=2,col=1)
    fig.update_xaxes(title_text="Indicator value",row=3,col=1)
    """
    update_layout is used to update the layout of the figure.
    height=800 sets the height of the figure to 800 pixels.
    title_text="Stock Chart with Technical Indicators" sets the title of the figure.
    xaxis_rangeslider_visible=False hides the range slider below the x-axis.
    showlegend=True shows the legend for the traces.
    update_xaxes is used to update the x-axis titles for each subplot."""

