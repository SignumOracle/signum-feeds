"""Datafeed for current price of WATT in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

watt_usd_median_feed = DataFeed(
    query=SpotPrice(asset="watt", currency="usd"),
    source=PriceAggregator(
        asset="watt",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="powercity-watt", currency="usd"),
        ],
    ),
)
