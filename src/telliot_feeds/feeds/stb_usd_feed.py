"""Datafeed for current price of STB in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price.spot.coinpaprika import CoinpaprikaSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

stb_usd_median_feed = DataFeed(
    query=SpotPrice(asset="stb", currency="usd"),
    source=PriceAggregator(
        asset="stb",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="stb", currency="usd"),
            CoinpaprikaSpotPriceSource(asset="stb-signum", currency="usd"),
        ],
    ),
)
