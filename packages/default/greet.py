def main(args):
    message = "Hello, " + args.get("name", "World") + "!";
    print(message)
    return {
        "body": {"message": message}
    }
