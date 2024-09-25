"""Datafeed for current price of BNB in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

bnb_usd_median_feed = DataFeed(
    query=SpotPrice(asset="bnb", currency="usd"),
    source=PriceAggregator(
        asset="bnb",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="binancecoin", currency="usd"),
        ],
    ),
)
