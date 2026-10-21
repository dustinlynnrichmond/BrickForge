# BrickForge — complete product specification

## Approved visual direction
- Use the user's approved realistic 3D brick icon-picker screenshot as the **art direction reference**, not as a sprite sheet or actual installable icon set.
- All app icons use matching realistic molded-plastic bricks: visible circular studs, beveled edges, construction seams, subtle wear-free gloss, directional highlights, depth and contact shadows.
- Symbols are **physically brick-built**, not flat logos pasted over a brick rectangle.
- Preserve recognizable silhouettes and color palettes where permitted; never substitute initials for known apps.
- Consistent padding, optical alignment, aspect ratio and Android adaptive icon safe area; export at multiple resolutions.
- Provide dark/light, matte/gloss, stud-density, bevel-depth, icon-shape, background and color controls.
- The app picker mockup is a reference; actual system app picker UI is controlled by Android/Samsung.

## App icon catalog
Initial coverage: Uber, Tasks, Peacock, Photos, SmartThings, eBay, Google Earth, Suno, Newegg, Steam Link, Plague Inc., Costco, Maps, Gallery, Facebook, Disney+, Assistant, Translate, UPS and Discover.
Expand to major installed Samsung, Google, Microsoft, social, messaging, gaming, streaming, shopping, finance, navigation, utility and productivity apps. Match **Android component/package IDs**, not display labels. Maintain a tested appfilter.xml with drawable references and app launch validation.

## Missing and newly installed apps
Detect changes with supported package visibility APIs and refresh coverage. Show per-app coverage and a manual icon picker. Unknown apps receive an **explicitly labeled** generic brick fallback until a matching icon is produced; do not claim automatic photo-realistic conversion of arbitrary app logos without an actual supported conversion pipeline.

## Customization and themes
- Preset theme palettes, individual icon overrides, randomize-with-preview, restore defaults, import/export user presets.
- Home screen wallpapers: creative brick worlds, seasonal environments, families and pets of varied appearances, customizable scenes, color variations, day/night and device aspect ratios.
- Brick-style widgets: clock, calendar, weather (with a configured data provider), battery, shortcuts, notes, photo frame, countdown, habits, music controls (where supported).
- Matching folder preview styles and app-drawer icon assets **where launcher supports it**.
- Accessible contrast, reduced-motion, large text, screen-reader labels, battery-conscious rendering.
- Preview and onboarding: before/after, coverage count, install instructions, errors and compatibility warnings.

## Samsung / Android
- Prioritize Galaxy S23 Ultra and stock Samsung One UI through Good Lock / Theme Park icon-pack import **only where supported**.
- Include a standard icon-pack implementation and appfilter mapping for compatible launchers; Theme Park import must be tested on device.
- A normal APK cannot silently replace icons for every installed app or control the system app picker.
- Support Android versions and target SDK required by the distribution store, subject to current verification.
- Samsung Keyboard / Keys Cafe customization is a separate deliverable, not a capability automatically provided by icon-pack APK.
- Optional custom keyboard requires a separate user-enabled IME, privacy review, input security and explicit consent. Never log typed text.
- Do not request broad package visibility without a defensible store-policy use case.

## iOS
iOS does not allow replacing every other app's launcher icon globally. Offer supported Shortcuts icon assets and optional instructions. Widgets and wallpapers require iOS-specific implementation; Android APKs do not run on iOS.

## Business and release
- Free previews and starter packs; premium optional theme packs and personalization tools, subject to transparent pricing and store policy.
- App must function without deceptive permissions, dark patterns or false one-tap claims.
- Maintain rights documentation for third-party logos and original artwork; no toy-company trademarks in public branding.
- Store listing: real screenshots, privacy policy, terms, support contact, compatibility matrix, clear premium disclosures.
- Provide crash reporting only with privacy-conscious configuration and consent as required.

## Definition of done
On supported devices, the user can install the APK, preview the full theme, import and apply supported icon assets, launch mapped apps, manually resolve missing icons, change supported colors and restore defaults. Automated build, resource validation and real-device acceptance tests pass.
