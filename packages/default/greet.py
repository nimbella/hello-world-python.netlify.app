def main(args):
    message = "Hello, " + args.get("name", "World") + "!";
    return {
        "body": {"message": message}
    }
