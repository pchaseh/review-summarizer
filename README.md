# review-summarizer

## Description
Aggregates reviews for a product and then produces a summarization

## Setup
Provide an OpenAI API key as follows:
```bash
$ export OPENAI_API_KEY="your_api_key_here"
```

To install the project and its dependencies:
```bash
$ poetry install
```

## Usage
```bash
$ python -m review_summarizer -p "Razer Opus X"
The reviews for the headset present a mixed bag of experiences. On the positive side, many users describe it as an "absolutely beautiful" headset, highlighting its lightweight design, user-friendliness, comfort, and attractive color. The audio quality is praised, along with a long-lasting battery life, especially for PC and mobile gaming. However, compatibility issues arise for those looking to use it with a PS4, as it is noted to be incompatible and made for PC/Mobile only, which has led to frustration among buyers.

On the downside, numerous complaints revolve around the build quality. Users report issues such as cracking after minimal use, static noises, and a general lack of durability. Some have experienced multiple pairs breaking in similar ways and have expressed dissatisfaction with the warranty process. Concerns over the materials used, particularly cheap plastic, have further dampened the overall perception of the product. Ultimately, while the headset has appealing features, its reliability and compatibility for console gaming have led to significant buyer disappointment.
```

## Support
Accuracy is contingent on being capable of pulling reviews for a product from multiple online websites. Unfortunately, often times these are gated by captcha mechanisms or require browser imitation techniques.
Additional review website sources may be added by deriving from the `ReviewQuerier` class and implementing the relevant functionality in the `reviews` method.
