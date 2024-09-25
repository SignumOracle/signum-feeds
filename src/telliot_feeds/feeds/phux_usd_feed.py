"""Datafeed for current price of PHUX in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

phux_usd_median_feed = DataFeed(
    query=SpotPrice(asset="phux", currency="usd"),
    source=PriceAggregator(
        asset="phux",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="phux-governance-token", currency="usd"),
        ],
    ),
)
