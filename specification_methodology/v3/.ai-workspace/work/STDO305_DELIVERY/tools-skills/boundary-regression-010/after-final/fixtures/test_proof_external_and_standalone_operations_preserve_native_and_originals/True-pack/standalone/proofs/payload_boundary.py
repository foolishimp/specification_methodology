"""Filesystem-identity boundary shared by installed STDO output commands."""
from __future__ import annotations

import os
from pathlib import Path


def ordinary(value):
    path = Path(value).absolute()
    if '..' in path.parts or any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('redirected/traversing output boundary path')
    return path


def same(left, right):
    return left.exists() and right.exists() and os.path.samefile(left, right)


def native_roots(anchors):
    """Recognize the installed logical routes by identity, never spelling.

    The method contract places tooling and proof entrypoints at these routes.
    Comparing each physical ancestor with its corresponding canonical route
    handles aliases on a case-insensitive volume without conflating distinct
    directories on a case-sensitive volume. Standalone bundles have no such
    enclosing route and retain their ordinary input-directory boundary.
    """
    roots = []
    routes = (Path('standards/tooling'), Path('standards/documentation/proofs'))
    for anchor in anchors:
        path = ordinary(anchor)
        for node in (path, *path.parents):
            if not node.is_dir():
                continue
            for route in routes:
                depth = len(route.parts)
                if len(node.parents) < depth:
                    continue
                candidate = node.parents[depth - 1]
                if same(node, candidate / route) and not any(same(candidate, prior) for prior in roots):
                    roots.append(candidate)
    return roots


def separate(output, protected):
    output, protected = ordinary(output), ordinary(protected)
    if output.is_relative_to(protected) or protected.is_relative_to(output):
        raise ValueError('output overlaps protected input or immutable native installation')
    for one, other in ((output, protected), (protected, output)):
        if any(same(parent, other) for parent in (one, *one.parents)):
            raise ValueError('output aliases protected input or immutable native installation')


def guard(outputs, inputs=(), *, anchors=()):
    """Validate the complete output set before any mkdir, copy or subprocess."""
    outputs = [ordinary(p) for p in outputs]
    inputs = [ordinary(p) for p in inputs]
    roots = native_roots([Path(__file__).absolute(), *inputs, *anchors])
    for output in outputs:
        for protected in [*inputs, *roots]:
            separate(output, protected)
    return roots
