from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.local_db_service import LocalDbService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    config_service = ConfigService()

    if args.openai_key:
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
        return None

    if args.reset:
        # reset the db the entire db
        LocalDbService().reset_db();
        Logger().log("OpenAI API key has been reset")
        return None

    if args.logger is not None:
        config_service.set_logger_enabled(args.logger)
        Logger().log("Logger " + ("enabled" if args.logger else "disabled"))
        return None

    display_config_db = LocalDbService().display_db()
    Logger().log(display_config_db)

    return None
