"""Datafeed for current price of TETRAP in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

tetrap_usd_median_feed = DataFeed(
    query=SpotPrice(asset="tetrap", currency="usd"),
    source=PriceAggregator(
        asset="tetrap",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="tetra", currency="usd"),
        ],
    ),
)
