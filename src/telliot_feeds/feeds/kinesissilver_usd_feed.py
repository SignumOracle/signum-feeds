"""Datafeed for current price of KINESIS SILVER in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

kinesissilver_usd_median_feed = DataFeed(
    query=SpotPrice(asset="kinesissilver", currency="usd"),
    source=PriceAggregator(
        asset="kinesissilver",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="kinesis-silver", currency="usd"),
        ],
    ),
)
