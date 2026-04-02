# Logo Assets

This directory contains all logo variations and sizes for the Vektori Memory Stack logo.

## 📁 Directory Structure

```
logo/
├── memory-stack-logo.svg                  # Main logo (dark background)
├── memory-stack-logo-transparent.svg      # Transparent background
├── memory-stack-logo-light.svg            # Light background variant
├── memory-stack-logo-monochrome.svg       # Monochrome/grayscale version
├── favicon/                               # Favicon sizes
│   ├── favicon-16x16.png
│   ├── favicon-32x32.png
│   └── favicon-48x48.png
├── app-icons/                             # PWA/App icons
│   ├── icon-192x192.png
│   └── icon-512x512.png
├── social/                                # Social media assets
│   ├── social-400x400.png
│   ├── social-400x400-light.png
│   ├── social-1200x1200.png
│   └── social-1200x1200-light.png
└── misc/                                  # General purpose sizes
    ├── logo-64x64.png
    ├── logo-128x128.png
    └── logo-256x256.png
```

## 🎨 Logo Variants

### 1. **Dark Background** (`memory-stack-logo.svg`)
- Use for: Favicons, dark mode UIs
- Background: #0f0f0f
- Color: #FF8204

### 2. **Transparent Background** (`memory-stack-logo-transparent.svg`)
- Use for: App icons, overlays, flexible contexts
- Background: None
- Color: #FF8204

### 3. **Light Background** (`memory-stack-logo-light.svg`)
- Use for: Light mode UIs, documents, presentations
- Background: #FFFFFF
- Color: #FF8204

### 4. **Monochrome** (`memory-stack-logo-monochrome.svg`)
- Use for: Print, limited color contexts
- Background: #0f0f0f
- Color: #FFFFFF (white)

## 🚀 Quick Usage Examples

### HTML/Web
```html
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/assets/logo/memory-stack-logo.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/logo/favicon/favicon-32x32.png">

<!-- Regular image -->
<img src="/assets/logo/misc/logo-128x128.png" alt="Vektori Logo" width="64" height="64">
```

### Next.js Metadata
```typescript
export const metadata: Metadata = {
  icons: {
    icon: [
      { url: '/assets/logo/favicon/favicon-16x16.png', sizes: '16x16' },
      { url: '/assets/logo/favicon/favicon-32x32.png', sizes: '32x32' },
    ],
    apple: '/assets/logo/app-icons/icon-192x192.png',
  },
}
```

### PWA Manifest
```json
{
  "icons": [
    {
      "src": "/assets/logo/app-icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/assets/logo/app-icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

### Social Media Meta Tags
```html
<!-- Open Graph -->
<meta property="og:image" content="/assets/logo/social/social-1200x1200.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="/assets/logo/social/social-1200x1200.png">
```

### Markdown (GitHub README)
```markdown
![Vektori Logo](public/assets/logo/misc/logo-128x128.png)
```

## 🛠️ Generating Assets

To regenerate PNG assets from SVG sources:

```bash
# Install dependencies
npm install sharp --save-dev

# Run the generator script
node scripts/generate-logo-assets.js
```

This will create all PNG sizes from the SVG sources.

## 📦 Recommended Sizes by Use Case

| Use Case | Recommended Size | File |
|----------|-----------------|------|
| **Browser Favicon** | 32x32, 16x16 | `favicon/favicon-*.png` |
| **PWA Icon** | 192x192, 512x512 | `app-icons/icon-*.png` |
| **Social Share** | 1200x1200 | `social/social-1200x1200.png` |
| **GitHub Avatar** | 400x400 | `social/social-400x400.png` |
| **Documentation** | 64x64, 128x128 | `misc/logo-*.png` |
| **App Store** | 512x512 | `app-icons/icon-512x512.png` |

## 🎯 Logo Design Concept

The Memory Stack logo represents:
- **Layered Blocks**: Stacked layers of memory and context
- **3D Perspective**: Depth and dimensionality of knowledge
- **Vertical Connections**: Linked information across layers
- **Progressive Opacity**: Building up from foundational to recent context

## 📄 License

Same as the Vektori project.
