"""Datafeed for current price of DAI-PULSECHAIN in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

daipulsechain_usd_median_feed = DataFeed(
    query=SpotPrice(asset="dai-pulsechain", currency="usd"),
    source=PriceAggregator(
        asset="dai-pulsechain",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="dai-pulsechain", currency="usd"),
        ],
    ),
)
