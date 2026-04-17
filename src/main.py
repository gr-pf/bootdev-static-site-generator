from pathlib import Path
import shutil

from generate_content_html import generate_page


def main():
    dest = Path("./public")
    del_dir(list(dest.iterdir()))

    src = Path("./static")
    for dir in list(src.iterdir()):
        copy_dir(dir, src, dest)
    for item in src.glob("**/*"):
        copy_file(item, src, dest)

    content_path = Path("./content")
    destination_path = Path("./public")
    print(content_path)
    for file in content_path.glob("**/*.md"):
        from_path = file
        template_path = "template.html"
        dest_path = destination_path / file.relative_to(content_path)
        generate_page(from_path, template_path, dest_path)
        dest_path.rename(dest_path.with_suffix(".html"))


def del_dir(paths):
    for path in paths:
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            del_dir(list(path.iterdir()))
            path.rmdir()


def copy_dir(path, src, dest):
    if path.is_file():
        return
    if path.is_dir():
        new_dir = dest / path.relative_to(src)
        if not new_dir.exists():
            new_dir.mkdir()
        for child_path in list(path.iterdir()):
            copy_dir(child_path, src, dest)
    return


def copy_file(path, src, dest):
    if path.is_dir():
        return
    if path.is_file():
        new_dest = dest / path.relative_to(src)
        shutil.copy(path, new_dest)


if __name__ == "__main__":
    main()
