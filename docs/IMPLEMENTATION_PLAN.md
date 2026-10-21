# Implementation and verification plan

## Phase 0 — clean project
- Create a new Android Studio project with Kotlin, Gradle Kotlin DSL, version catalog and pinned Android Gradle Plugin.
- Use a unique application ID, BrickForge branding, clean manifest, no inherited legacy generator or ZIP extraction.
- Decide supported minimum SDK and current Play/Samsung store target SDK before release.
- Add licenses, privacy policy, dependency checks and project documentation.

## Phase 1 — icon assets
- Create approved master artwork for each app; the reference screenshot is **not** itself a usable icon atlas.
- Store editable source artwork plus exported 512px PNG and density-appropriate output assets.
- Use a deterministic renderer only when it produces the approved **brick-built** look. No monograms.
- Build package/component-to-drawable mapping and catalog; validate no duplicate or missing drawables.
- Support unknown-app fallback, manual overrides and coverage reporting.
- Add visual snapshot tests for lighting, contrast, padding, color and stud geometry.

## Phase 2 — working Android icon pack
- Android activity: theme gallery, preview, compatibility check, installed-app coverage, customization, settings and help.
- Launcher/icon-pack metadata (appfilter.xml, drawable.xml and intents as required).
- Verify Samsung Good Lock / Theme Park icon import on real Galaxy S23 Ultra; document unsupported One UI versions.
- Verify mapped app launches, uninstall/install refresh, theme persistence and restore.

## Phase 3 — extended personalization
- Brick-scene wallpaper gallery with aspect-ratio previews, export and supported wallpaper application.
- App widgets built with Android AppWidget APIs, responsive layout and updates.
- Keyboard options: exported compatible theme assets or separately developed IME, no unsupported automatic system changes.
- Presets, palette editor, favorites, backups, restore and optional premium catalog.

## Phase 4 — release readiness
- Unit tests, instrumentation tests, lint, dependency audits and accessibility review.
- Test battery usage, memory, icon cropping, dark mode, permissions, new installs and system updates.
- Signed AAB/APK process with secure signing keys, release notes, versioning, reproducible builds.
- Samsung Galaxy Store and Play policy checks, privacy policy, rights audit, support channel.
- iOS companion/Shortcuts export is a separate project.

## CI acceptance criteria
- Gradle project present and builds with a supported JDK.
- No missing icon resources or invalid appfilter entries.
- Debug APK artifact uploaded only after successful build.
- Never mark a successful build as evidence of Theme Park compatibility without a real-device test.

## Known risks
Samsung Theme Park import availability changes across One UI versions; third-party logos may need permission; iOS icon limitations; keyboard restrictions; performance impact of high-resolution assets; asset generation cost and app-package mapping drift.

## Current status
Specifications and workflow scaffolding only. No verified APK or full 3D artwork catalog yet.
