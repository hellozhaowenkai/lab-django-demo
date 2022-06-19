import os


def __organize_settings():
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib

    config_path = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(config_path, "settings.toml"), "rb") as f:
        main_settings = tomllib.load(f)
    sensitive_settings = main_settings.setdefault("sensitive-settings", {})

    if not sensitive_settings.setdefault("enabled", False):
        return main_settings

    for patch in sensitive_settings.setdefault("includes", []):
        patch_namespace = patch.get("namespace", "secrets")
        patch_filename = patch.get("filename", "settings.private.toml")
        patch_path = os.path.join(config_path, patch_filename)

        if os.path.isfile(patch_path):
            with open(os.path.join(patch_path), "rb") as f:
                patch_settings = tomllib.load(f)
        else:
            patch_settings = {}

        main_settings.setdefault(patch_namespace, {}).update(patch_settings)

    return main_settings


settings = __organize_settings()

__all__ = [settings]
