from os import getcwd

from dynaconf import Dynaconf

config = Dynaconf(
    dotenv_override=True,
    encoding="utf-8",
    environments=False,
    envvar_prefix=False,  # won't use a prefix at all
    load_dotenv=True,  # .env file is automatically detected and loaded
    root_path="etc",
)

print("Hello!")
print(getcwd())

print(config.dynaconf_include)
print(config.name)
print(config.age)
