import argparse
from openai import OpenAI
from review_summarizer.query.bestbuy_ca import BestBuyCAReviewQuerier

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m", "--openai-model", type=str, default="gpt-4o-mini", help="OpenAI model to use"
)
parser.add_argument(
    "-p", "--product", type=str, required=True, help="Product name to query"
)

args = parser.parse_args()

querier_classes = [BestBuyCAReviewQuerier]

client = OpenAI()


def main():
    reviews = []
    for querier_cls in querier_classes:
        querier = querier_cls()
        reviews.extend(querier.reviews(args.product))

    if len(reviews) == 0:
        print("No reviews found for '%s'", args.product)
        return

    completion = client.chat.completions.create(
        model=args.openai_model,
        messages=[
            {"role": "system", "content": "Create a summary of the reviews"},
            {"role": "user", "content": "\n".join(reviews)},
        ],
    )

    print(completion.choices[0].message.content)


main()
