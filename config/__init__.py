def __organize_settings():
    import os
    import toml

    config_path = os.path.abspath(os.path.dirname(__file__))
    main_settings = toml.load(os.path.join(config_path, "settings.toml"))

    sensitive_settings = main_settings.setdefault("sensitive-settings", {})
    if not sensitive_settings.setdefault("enabled", False):
        return main_settings

    for patch in sensitive_settings.setdefault("includes", []):
        patch_namespace = patch.get("namespace", "secrets")
        patch_filename = patch.get("filename", "settings.private.toml")
        patch_path = os.path.join(config_path, patch_filename)
        patch_settings = toml.load(patch_path) if os.path.isfile(patch_path) else {}
        main_settings.setdefault(patch_namespace, {}).update(patch_settings)

    return main_settings


settings = __organize_settings()

__all__ = [settings]
