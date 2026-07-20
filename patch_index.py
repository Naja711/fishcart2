import sys

# Define replacement strings

NEW_STYLES = """  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&amp;display=swap" rel="stylesheet"/>
  <style>
    *::-webkit-scrollbar {
      display: none;
    }

    * {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    *,
    *::before,
    *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', 'Inter', sans-serif !important;
    }

    html,
    body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: 'Poppins', 'Inter', sans-serif !important;
      background: #E8F3FA;
    }

    :root {
      --navy-blue: #0f46bd;
      --sidebar-active: #0350dc;
      --hero-btn: #123e97;
      --fish-card: #79c4fd;
      --meat-card: #fd7975;
      --chicken-card: #feb33c;
      --eggs-banner-start: #f1ffe3;
      --eggs-banner-end: #d2eda9;
      --recipes-card: #0350dc;
      --benefits-card: #ebf5ff;
      --reviews-card: #eef6ff;
      --star-gold: #f6c214;
      --freshness-card: #4ba5fb;
      --hygienic-card: #b6f2ff;
      --sourced-card: #d2eda9;
      --community-card: #c1e1ff;
      --frame-border: #2c79e3;
      --text-navy: #0f46bd;
      --text-gray: #5b6472;

      /* Compatibility variables for list pages */
      --primary-color: #0350dc;
      --light-bg: #EAF2FF;
      --border-color: #cbd5e1;
      --text-main: #0f46bd;
      --text-light: #5b6472;
      --bg-color: #F8FAFC;
      --white: #FFFFFF;
    }

    /* Outer Frame Layout */
    .app {
      display: flex;
      flex-direction: column;
      width: 1448px;
      height: 1086px;
      border: 16px solid var(--frame-border);
      border-radius: 24px;
      background: #ffffff;
      overflow: hidden;
      position: fixed;
      top: 0;
      left: 0;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
      box-sizing: border-box;
      transform-origin: top left;
    }

    /* ── HEADER ── */
    .main-header {
      height: 75px;
      background: #ffffff;
      border-bottom: 1.5px solid #e2e8f0;
      display: flex;
      align-items: center;
      padding: 0 24px;
      z-index: 110;
      flex-shrink: 0;
    }

    .logo-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .logo-icon {
      width: 28px;
      height: 28px;
      flex-shrink: 0;
    }

    .logo-text {
      display: flex;
      flex-direction: column;
      line-height: 1.25;
    }

    .logo-title {
      font-size: 20px;
      font-weight: 900;
      color: var(--text-navy);
      letter-spacing: 0.5px;
    }

    .logo-subtitle {
      font-size: 10px;
      color: var(--sidebar-active);
      font-weight: 500;
    }

    /* ── MAIN LAYOUT ── */
    .main-container {
      display: flex;
      flex: 1;
      min-height: 0;
      position: relative;
      background: #ffffff;
    }

    /* ── SIDEBAR ── */
    .sidebar {
      width: 250px;
      background: #ffffff;
      border-right: 1.5px solid #e2e8f0;
      padding: 20px 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex-shrink: 0;
      overflow-y: auto;
      height: 100%;
    }

    .sidebar-freshness {
      background: linear-gradient(135deg, #1565C0 0%, #0d47a1 100%);
      border-radius: 16px;
      padding: 16px;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: auto;
      box-shadow: 0 4px 12px rgba(15, 70, 189, 0.15);
      flex-shrink: 0;
    }
    .sb-fresh-text { display: flex; flex-direction: column; gap: 5px; }
    .sb-fresh-title {
      font-size: 14px;
      font-weight: 800;
      line-height: 1.2;
    }
    .sb-fresh-desc {
      font-size: 10px;
      color: rgba(255, 255, 255, 0.85);
      line-height: 1.45;
    }
    .sb-fresh-icon {
      width: 38px;
      height: 38px;
      background: rgba(255,255,255,0.18);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 1px solid rgba(255,255,255,0.25);
    }
    .sb-fresh-icon svg { width: 18px; height: 18px; }

    .nav {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .ni {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border-radius: 12px;
      cursor: pointer;
      color: var(--text-navy);
      font-size: 13.5px;
      font-weight: 600;
      transition: all 0.2s ease;
      white-space: nowrap;
      border: 1.5px solid #e2e8f0;
      background: #ffffff;
    }

    .ni:hover:not(.active) {
      border-color: var(--sidebar-active);
      color: var(--sidebar-active);
      background: #f8fafc;
    }

    .ni.active {
      background: var(--sidebar-active);
      color: #ffffff !important;
      border-color: var(--sidebar-active);
      box-shadow: 0 4px 12px rgba(3, 80, 220, 0.25);
    }

    .ni svg {
      width: 18px;
      height: 18px;
      flex-shrink: 0;
    }

    #nav-home svg { color: #0350dc; stroke: #0350dc; }
    #nav-fish svg { color: #0350dc; stroke: #0350dc; }
    #nav-meat svg { color: #e11d48; stroke: #e11d48; }
    #nav-chicken svg { color: #f97316; stroke: #f97316; }
    #nav-eggs svg { color: #eab308; stroke: #eab308; }
    #nav-cook svg { color: #0350dc; stroke: #0350dc; }
    #nav-benefits svg { color: #0350dc; stroke: #0350dc; }
    #nav-stories svg { color: #0350dc; stroke: #0350dc; }
    #nav-about svg { color: #0350dc; stroke: #0350dc; }
    #nav-contact svg { color: #0350dc; stroke: #0350dc; }

    .ni.active svg {
      color: #ffffff !important;
      stroke: #ffffff !important;
    }

    /* ── CONTENT AREA ── */
    .content-area {
      flex: 1;
      min-width: 0;
      height: 100%;
      overflow-y: auto;
      position: relative;
      background: #ffffff;
    }

    /* ── PAGE SYSTEM ── */
    .page {
      display: none;
      width: 100%;
      height: 100%;
      overflow-y: auto;
    }

    .page.active {
      display: flex;
      flex-direction: column;
    }

    /* ── HOME VIEW ── */
    .home {
      padding: 16px 20px;
      display: grid;
      grid-template-rows: 3.2fr 2.6fr 1.7fr 1.3fr 1.2fr;
      gap: 10px;
      background: #ffffff;
      flex: 1;
      min-height: 0;
      overflow: hidden;
      box-sizing: border-box;
    }

    /* ROW 1: Hero & Category grid */
    .r1 {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 14px;
      overflow: hidden;
      min-height: 0;
    }

    /* Hero Banner */
    .hero {
      background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
      border-radius: 16px;
      padding: 20px 24px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      box-sizing: border-box;
    }

    .h1 {
      font-size: 22px;
      font-weight: 800;
      color: #0A2848;
      line-height: 1.2;
    }

    .hp {
      font-size: 11px;
      color: #2a5070;
      margin: 5px 0 10px;
    }

    .hero-img {
      position: absolute;
      right: 0;
      top: 0;
      bottom: 0;
      height: 100%;
      width: 44%;
      object-fit: cover;
      object-position: center center;
      border-radius: 0 16px 16px 0;
      -webkit-mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.6) 22%, black 42%);
      mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.6) 22%, black 42%);
    }

    .btn-join {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--hero-btn);
      color: #ffffff;
      border: none;
      padding: 10px 22px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.2s;
      width: fit-content;
    }

    .btn-join:hover {
      background: #0d2f70;
    }

    .hero-badges {
      display: flex;
      gap: 10px;
      margin-top: 10px;
      z-index: 2;
    }

    .hb {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .hbc {
      width: 20px;
      height: 20px;
      border-radius: 5px;
      border: 1.5px solid #1565C0;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #1565C0;
      flex-shrink: 0;
    }

    .hbc svg {
      width: 14px;
      height: 14px;
    }

    .hbl {
      font-size: 10px;
      color: #2a5070;
      font-weight: 700;
      line-height: 1.25;
    }

    /* Right Column Category/Eggs Grid */
    .cat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 16px;
      height: 100%;
    }

    .cat {
      border-radius: 16px;
      padding: 16px;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
      height: 100%;
      border: 1px solid #e2e8f0;
    }

    .cat:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    }

    .cat.fish {
      background: var(--fish-card);
    }

    .cat.meat {
      background: var(--meat-card);
    }

    .cat.chicken {
      background: var(--chicken-card);
    }

    .cat.eggs {
      background: linear-gradient(135deg, var(--eggs-banner-start) 0%, var(--eggs-banner-end) 100%);
      grid-column: span 3;
      flex-direction: row;
      align-items: center;
      height: 100%;
    }

    .cat-inf {
      z-index: 2;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }

    .cat.eggs .cat-inf {
      flex-direction: row;
      align-items: center;
      width: 100%;
    }

    .cat-name {
      font-size: 16px;
      font-weight: 800;
      color: var(--text-navy);
    }

    .cat.eggs .cat-name {
      font-size: 20px;
    }

    .cat-cnt {
      font-size: 11px;
      color: var(--text-navy);
      font-weight: 500;
      margin-top: 2px;
    }

    .cat.eggs .cat-cnt {
      font-size: 13px;
      margin-top: 0;
      margin-left: 8px;
    }

    .cat-arr {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-navy);
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
      transition: all 0.2s;
    }

    .cat:hover .cat-arr {
      background: var(--sidebar-active);
      color: #ffffff;
    }

    .cimg {
      position: absolute;
      right: 4px;
      bottom: 0;
      height: 70%;
      width: auto;
      object-fit: contain;
      z-index: 1;
    }

    .cat.eggs .cimg {
      height: 100%;
      right: 40px;
    }

    /* ROW 2: Recipes + Benefits + Reviews */
    .r2 {
      display: grid;
      grid-template-columns: 1.4fr 1.2fr 1fr;
      gap: 14px;
      overflow: hidden;
      min-height: 0;
    }

    .recipes-card {
      background: var(--recipes-card);
      border-radius: 16px;
      padding: 14px;
      color: #ffffff;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      height: 100%;
      box-sizing: border-box;
    }

    .recipes-card .card-title {
      font-size: 14px;
      font-weight: 800;
    }

    .recipes-card .card-subtitle {
      font-size: 10px;
      color: rgba(255,255,255,0.85);
      margin-top: 2px;
    }

    .video-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 8px 0;
    }

    .video-item {
      display: flex;
      flex-direction: column;
      gap: 6px;
      cursor: pointer;
    }

    .video-thumbnail {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      aspect-ratio: 4/3;
    }

    .video-thumbnail img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .play-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }

    .video-item:hover .play-overlay {
      background: rgba(0,0,0,0.35);
    }

    .play-icon {
      width: 24px;
      height: 24px;
      background: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--sidebar-active);
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

    .play-icon svg {
      width: 10px;
      height: 10px;
      margin-left: 2px;
    }

    .video-label {
      font-size: 11px;
      font-weight: 700;
    }

    .view-all-btn {
      background: #ffffff;
      color: var(--sidebar-active);
      border: none;
      padding: 8px 16px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      width: fit-content;
      transition: all 0.2s;
    }

    .view-all-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    /* Benefits Card */
    .benefits-card {
      background: var(--benefits-card);
      border-radius: 16px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid #e2e8f0;
      overflow: hidden;
      height: 100%;
      box-sizing: border-box;
    }

    .benefits-card .card-title {
      font-size: 13px;
      font-weight: 800;
      color: var(--text-navy);
    }

    .benefits-card .card-content {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 6px 0;
    }

    .benefits-card .card-text {
      flex: 1;
    }

    .benefits-card .card-desc {
      font-size: 11px;
      color: var(--text-gray);
      line-height: 1.45;
    }

    .benefits-card .learn-more-link {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 700;
      color: var(--sidebar-active);
      margin-top: 8px;
      cursor: pointer;
    }

    .benefits-card .benefits-img {
      width: 65px;
      height: 65px;
      object-fit: cover;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .benefits-card .badge-row {
      display: flex;
      justify-content: space-between;
      gap: 8px;
    }

    .benefit-badge {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      text-align: center;
      flex: 1;
    }

    .benefit-badge-icon {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--sidebar-active);
      box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }

    .benefit-badge-icon svg {
      width: 14px;
      height: 14px;
    }

    .benefit-badge-label {
      font-size: 9px;
      font-weight: 700;
      color: var(--text-gray);
      line-height: 1.2;
    }

    /* Reviews Card */
    .reviews-card {
      background: var(--reviews-card);
      border-radius: 16px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid #e2e8f0;
      position: relative;
      overflow: hidden;
      height: 100%;
      box-sizing: border-box;
    }

    .reviews-card .quote-icon {
      font-size: 48px;
      font-weight: 900;
      color: var(--text-navy);
      position: absolute;
      top: -10px;
      left: 14px;
      opacity: 0.15;
    }

    .reviews-card .card-title {
      font-size: 13px;
      font-weight: 800;
      color: var(--text-navy);
      margin-top: 6px;
    }

    .reviews-card .stars {
      color: var(--star-gold);
      font-size: 12px;
      margin: 4px 0;
    }

    .reviews-card .testimonial-text {
      font-size: 11.5px;
      font-style: italic;
      color: var(--text-gray);
      line-height: 1.5;
      flex: 1;
    }

    .reviews-card .attribution {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-navy);
      margin-top: 10px;
    }

    .reviews-card .dots-container {
      display: flex;
      gap: 6px;
      margin-top: 12px;
    }

    .reviews-card .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #cbd5e1;
      cursor: pointer;
      transition: all 0.2s;
    }

    .reviews-card .dot.active {
      background: var(--sidebar-active);
      width: 14px;
      border-radius: 3px;
    }

    /* ROW 3: Product Grid (Showcase) */
    .r3 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      overflow: hidden;
      min-height: 0;
    }

    .product-tile {
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
      height: 100%;
    }

    .product-tile img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }

    .product-tile:hover img {
      transform: scale(1.05);
    }

    .scrim {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 60%);
    }

    .tile-content {
      position: absolute;
      left: 16px;
      bottom: 16px;
      right: 16px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      color: #ffffff;
      z-index: 2;
    }

    .tile-label {
      font-size: 14px;
      font-weight: 800;
    }

    .tile-link {
      font-size: 10px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
      background: rgba(255,255,255,0.2);
      padding: 4px 10px;
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.3);
      transition: background 0.2s;
    }

    .product-tile:hover .tile-link {
      background: rgba(255,255,255,0.3);
    }

    /* ROW 4: Features */
    .r4 {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      overflow: hidden;
      min-height: 0;
    }

    .feature-card {
      border-radius: 16px;
      padding: 12px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.02);
      border: 1px solid #cbd5e1;
      overflow: hidden;
    }

    .feature-card .feat-text {
      display: flex;
      flex-direction: column;
      gap: 3px;
      flex: 1;
      min-width: 0;
    }

    .feature-card .feat-title {
      font-size: 12.5px;
      font-weight: 800;
      line-height: 1.25;
    }

    .feature-card .feat-desc {
      font-size: 9.5px;
      line-height: 1.35;
    }

    .feature-card .icon-circle {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      flex-shrink: 0;
    }

    .feature-card.freshness {
      background: #3b82f6;
      border: 1px solid #3b82f6;
      color: #ffffff;
    }

    .feature-card.freshness .feat-title,
    .feature-card.freshness .feat-desc {
      color: #ffffff;
    }

    .feature-card.freshness .icon-circle {
      background: rgba(255, 255, 255, 0.2);
      border: 1.5px solid rgba(255, 255, 255, 0.4);
      color: #ffffff;
      box-shadow: none;
    }

    .feature-card.daily {
      background: #e4f2fd;
      border: 1px solid #d0e6f9;
      color: #0f46bd;
    }

    .feature-card.daily .feat-title { color: #0f46bd; }
    .feature-card.daily .feat-desc { color: #5b6472; }
    .feature-card.daily .icon-circle {
      background: #ffffff;
      border: 1.5px solid #0350dc;
      color: #0350dc;
    }

    .feature-card.hygienic {
      background: #b6f2ff;
      border: 1px solid #a2eaf9;
      color: #0f46bd;
    }

    .feature-card.hygienic .feat-title { color: #0f46bd; }
    .feature-card.hygienic .feat-desc { color: #334155; }
    .feature-card.hygienic .icon-circle {
      background: #ffffff;
      border: 1.5px solid #00bcd4;
      color: #00bcd4;
    }

    .feature-card.sourced {
      background: #d2eda9;
      border: 1px solid #c4e498;
      color: #0f46bd;
    }

    .feature-card.sourced .feat-title { color: #0f46bd; }
    .feature-card.sourced .feat-desc { color: #334155; }
    .feature-card.sourced .icon-circle {
      background: #ffffff;
      border: 1.5px solid #4caf50;
      color: #4caf50;
    }

    .feature-card.community {
      background: #c1e1ff;
      border: 1px solid #b0d8ff;
      color: #0f46bd;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
    }

    .community-left {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      gap: 4px;
    }

    .community-left .join-btn {
      background: var(--hero-btn);
      color: #ffffff;
      border: none;
      padding: 5px 12px;
      border-radius: 12px;
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      width: fit-content;
      transition: all 0.2s;
    }

    .community-left .join-btn:hover {
      background: #0d2f70;
    }

    /* Footer columns grid (Row 5) */
    .r5 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1.35fr;
      gap: 14px;
      overflow: hidden;
      min-height: 0;
      box-sizing: border-box;
    }

    .footer-card {
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 16px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      overflow: hidden;
      height: 100%;
      box-sizing: border-box;
    }

    .footer-card .fc-text {
      display: flex;
      flex-direction: column;
      gap: 3px;
      flex: 1;
      min-width: 0;
    }

    .footer-card .fc-title {
      font-size: 12.5px;
      font-weight: 800;
      color: #0f46bd;
    }

    .footer-card .fc-desc {
      font-size: 9.5px;
      color: #5b6472;
      line-height: 1.35;
    }

    .footer-card .fc-img {
      height: 48px;
      width: auto;
      max-width: 65px;
      object-fit: contain;
      flex-shrink: 0;
    }

    .footer-contact-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 9.5px;
      color: #5b6472;
      line-height: 1.3;
    }

    .footer-contact-item svg {
      width: 12px;
      height: 12px;
      color: var(--sidebar-active);
      flex-shrink: 0;
    }


    .mobile-filter-btn {
      display: none;
    }
    
    .filter-overlay {
      display: none;
    }

    /* ── MOBILE RESPONSIVENESS ── */
    @media (max-width: 768px) {
      body {
        height: 100vh;
        overflow: hidden;
      }

      .app {
        flex-direction: column;
        height: 100vh;
        overflow: hidden;
      }

      .sidebar {
        width: 100%;
        height: auto;
        flex-direction: row;
        overflow-x: auto;
        padding: 10px;
        z-index: 90;
      }

      .logo-area {
        display: none;
      }

      .nav {
        flex-direction: row;
        gap: 8px;
      }

      .ni {
        padding: 8px 12px;
        font-size: 12px;
      }

      .r1 {
        grid-template-columns: 1fr 1fr;
      }

      .r2 {
        grid-template-columns: 1fr;
      }

      .mobile-filter-btn {
        display: flex;
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        background: var(--primary-color);
        color: #ffffff;
        border-radius: 30px;
        padding: 14px 28px;
        font-weight: 700;
        font-size: 14px;
        z-index: 900;
        box-shadow: 0 4px 15px rgba(3, 80, 220, 0.4);
        cursor: pointer;
        align-items: center;
        gap: 8px;
      }
      
      .filter-overlay.active {
        display: block;
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
      }
    }
  </style>"""
NEW_BODY = """<body>
  <div class="app">
    <!-- Header -->
    <header class="main-header">
      <div class="logo-group">
        <svg class="logo-icon" viewBox="0 0 24 24" fill="none" stroke="#0f46bd" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M15 6l-6 6 6 6M21 6l-6 6 6 6" />
        </svg>
        <div class="logo-text">
          <span class="logo-title">FISHCART</span>
          <span class="logo-subtitle">Daily Fresh Partner</span>
        </div>
      </div>
    </header>

    <div class="main-container">
      <!-- Sidebar -->
      <aside class="sidebar">
        <nav class="nav">
          <div class="ni active" id="nav-home" onclick="go('home')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>Home
          </div>
          <div class="ni" id="nav-fish" onclick="go('fish')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M20 12c-2.5-4-5.5-5.5-8-5.5C9.5 6.5 6.5 8 4 12c2.5 4 5.5 5.5 8 5.5s5.5-1.5 8-5.5z"/><circle cx="15" cy="12" r="1"/><path d="M4 12l-2-2v4l2-2z"/>
            </svg>Fish
          </div>
          <div class="ni" id="nav-meat" onclick="go('meat')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M18.5 3.5A2.5 2.5 0 0016 1c-1.1 0-2 .9-2 2H10C10 1.9 9.1 1 8 1a2.5 2.5 0 00-2.5 2.5c0 1.12.74 2.07 1.75 2.4L6.5 7H5v14h14V7h-1.5l-.75-1.1a2.5 2.5 0 001.75-2.4z"/><circle cx="11" cy="12" r="2"/>
            </svg>Meat
          </div>
          <div class="ni" id="nav-chicken" onclick="go('chicken')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M17.5 4.5c-1.95 0-3.5 1.55-3.5 3.5 0 .72.23 1.38.6 1.93l-5.1 5.1c-.55-.37-1.21-.6-1.93-.6-1.95 0-3.5 1.55-3.5 3.5s1.55 3.5 3.5 3.5 3.5-1.55 3.5-3.5c0-.72-.23-1.38-.6-1.93l5.1-5.1c.55.37 1.21.6 1.93.6 1.95 0 3.5-1.55 3.5-3.5S19.45 4.5 17.5 4.5z"/>
            </svg>Chicken
          </div>
          <div class="ni" id="nav-eggs" onclick="go('eggs')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M12 2C8.13 2 5 7.9 5 12.5c0 3.87 3.13 7 7 7s7-3.13 7-7C19 7.9 15.87 2 12 2z"/><ellipse cx="11" cy="14" rx="2" ry="3"/>
            </svg>Eggs
          </div>
          <div class="ni" id="nav-cook" onclick="go('cook')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M6 13.87A6 6 0 017.41 2.41 6 6 0 0118 6a6 6 0 011.41 11.87L18 21H6l-1.41-3.13z"/><path d="M6 17h12"/>
            </svg>How to Cook
          </div>
          <div class="ni" id="nav-benefits" onclick="go('benefits')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l8.72-8.72 1.06-1.06a5.5 5.5 0 000-7.78z"/><path d="M12 8v4l3 3"/>
            </svg>Benefits
          </div>
          <div class="ni" id="nav-stories" onclick="go('stories')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/>
            </svg>Our Stories
          </div>
          <div class="ni" id="nav-about" onclick="go('about')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>
            </svg>About Us
          </div>
          <div class="ni" id="nav-contact" onclick="go('contact')">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/>
            </svg>Contact Us
          </div>
        </nav>
        
        <div class="sidebar-freshness">
          <div class="sb-fresh-text">
            <div class="sb-fresh-title">Freshness<br>You Can Trust</div>
            <div class="sb-fresh-desc">We ensure premium quality and freshness in every product we deliver.</div>
          </div>
          <div class="sb-fresh-icon">
            <svg fill="#ffffff" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
          </div>
        </div>
      </aside>

      <!-- Content Area -->
      <main class="content-area">
        <!-- ═══ HOME PAGE ═══ -->
        <div class="page active" id="page-home" style="overflow:hidden;">
          <div class="home">
            <!-- ROW 1: Hero + Category/Eggs Grid -->
            <div class="r1">
              <!-- Hero Banner -->
              <div class="hero">
                <div style="z-index:2; max-width: 250px;">
                  <h1 class="h1">Fresh Fish.<br/>Healthy Life.</h1>
                  <p class="hp">Handpicked daily for freshness you can trust.</p>
                  <button class="btn-join" onclick="go('about')">
                    Join Us
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:12px; height:12px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </button>
                </div>
                <img alt="Fresh Fish on Ice" class="hero-img" src="assets/fresh_fish_on_ice_1783634420753.png"/>

                <!-- Badges -->
                <div class="hero-badges">
                  <div class="hb">
                    <div class="hbc">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <path d="M8 12l3 3 5-5"></path>
                      </svg>
                    </div>
                    <span class="hbl">100%<br>Fresh</span>
                  </div>
                  <div class="hb">
                    <div class="hbc">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        <polygon points="12 8 13.5 11 17 11.5 14.5 14 15 17.5 12 16 9 17.5 9.5 14 7 11.5 10.5 11"></polygon>
                      </svg>
                    </div>
                    <span class="hbl">Hygienic<br>& Safe</span>
                  </div>
                  <div class="hb">
                    <div class="hbc">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="1" y="3" width="15" height="13"></rect>
                        <polygon points="16 8 20 8 23 11 23 16 16 16"></polygon>
                        <circle cx="5.5" cy="18.5" r="2.5"></circle>
                        <circle cx="18.5" cy="18.5" r="2.5"></circle>
                      </svg>
                    </div>
                    <span class="hbl">Daily<br>Delivery</span>
                  </div>
                  <div class="hb">
                    <div class="hbc">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="8" r="7"></circle>
                        <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                      </svg>
                    </div>
                    <span class="hbl">Best<br>Quality</span>
                  </div>
                </div>
              </div>

              <!-- Right Column: Categories + Eggs -->
              <div class="cat-grid">
                <div class="cat fish" onclick="go('fish')">
                  <div class="cat-inf">
                    <div>
                      <div class="cat-name">Fish</div>
                      <div class="cat-cnt">100+ Items</div>
                    </div>
                    <div class="cat-arr">
                      <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:12px; height:12px;">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                      </svg>
                    </div>
                  </div>
                  <img alt="Fish" class="cimg" src="assets/cat_fish.png"/>
                </div>
                <div class="cat meat" onclick="go('meat')">
                  <div class="cat-inf">
                    <div>
                      <div class="cat-name">Meat</div>
                      <div class="cat-cnt">50+ Items</div>
                    </div>
                    <div class="cat-arr">
                      <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:12px; height:12px;">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                      </svg>
                    </div>
                  </div>
                  <img alt="Meat" class="cimg" src="assets/cat_meat.png"/>
                </div>
                <div class="cat chicken" onclick="go('chicken')">
                  <div class="cat-inf">
                    <div>
                      <div class="cat-name">Chicken</div>
                      <div class="cat-cnt">30+ Items</div>
                    </div>
                    <div class="cat-arr">
                      <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:12px; height:12px;">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                      </svg>
                    </div>
                  </div>
                  <img alt="Chicken" class="cimg" src="assets/cat_chicken.png"/>
                </div>

                <div class="cat eggs" onclick="go('eggs')">
                  <div class="cat-inf">
                    <div>
                      <div class="cat-name">Eggs</div>
                      <div class="cat-cnt">Farm Fresh</div>
                    </div>
                    <div class="cat-arr">
                      <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:12px; height:12px;">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                      </svg>
                    </div>
                  </div>
                  <img alt="Eggs" class="cimg" src="assets/cat_eggs.png"/>
                </div>
              </div>
            </div>

            <!-- ROW 2: Recipes + Benefits + Reviews -->
            <div class="r2">
              <!-- Recipes Card -->
              <div class="recipes-card">
                <div>
                  <div class="card-title">How to Make Delicious</div>
                  <div class="card-subtitle">Step by step cooking videos for every taste</div>
                </div>
                <div class="video-grid">
                  <div class="video-item" onclick="go('cook')">
                    <div class="video-thumbnail">
                      <img alt="Fish Curry" src="https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&amp;fit=crop&amp;w=200&amp;q=80"/>
                      <div class="play-overlay">
                        <div class="play-icon">
                          <svg fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z"></path>
                          </svg>
                        </div>
                      </div>
                    </div>
                    <div class="video-label">Fish Curry</div>
                  </div>
                  <div class="video-item" onclick="go('cook')">
                    <div class="video-thumbnail">
                      <img alt="Grilled Fish" src="https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&amp;fit=crop&amp;w=200&amp;q=80"/>
                      <div class="play-overlay">
                        <div class="play-icon">
                          <svg fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z"></path>
                          </svg>
                        </div>
                      </div>
                    </div>
                    <div class="video-label">Grilled Fish</div>
                  </div>
                  <div class="video-item" onclick="go('cook')">
                    <div class="video-thumbnail">
                      <img alt="Fish Fry" src="https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&amp;fit=crop&amp;w=200&amp;q=80"/>
                      <div class="play-overlay">
                        <div class="play-icon">
                          <svg fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z"></path>
                          </svg>
                        </div>
                      </div>
                    </div>
                    <div class="video-label">Fish Fry</div>
                  </div>
                </div>
                <button class="view-all-btn" onclick="go('cook')">
                  View All Recipes
                  <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                    <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                  </svg>
                </button>
              </div>

              <!-- Benefits Card -->
              <div class="benefits-card">
                <div class="card-title">Benefits & Nutrition</div>
                <div class="card-content">
                  <div class="card-text">
                    <p class="card-desc">Fish, meat, eggs and chicken are rich in protein, vitamins and minerals for a stronger, healthier you.</p>
                    <a class="learn-more-link" onclick="go('benefits')">
                      Learn More
                      <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                        <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                      </svg>
                    </a>
                  </div>
                  <img alt="Healthy food" class="benefits-img" src="assets/benefits_salmon.png"/>
                </div>
                <div class="badge-row">
                  <div class="benefit-badge">
                    <div class="benefit-badge-icon">
                      <svg fill="currentColor" viewBox="0 0 24 24">
                        <path d="M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14 1.43 1.43 1.43-1.43-1.43-1.43L22 16.29z"></path>
                      </svg>
                    </div>
                    <span class="benefit-badge-label">High in<br/>Protein</span>
                  </div>
                  <div class="benefit-badge">
                    <div class="benefit-badge-icon">
                      <svg fill="currentColor" viewBox="0 0 24 24">
                        <path d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1-2.3A4.49 4.49 0 008 20c4 0 4-2 8-2s4 2 8 2v-2c-4 0-4-2-8-2-1.17 0-1.85.17-2.47.34C14.22 14.5 17.5 12 22 10V8z"></path>
                      </svg>
                    </div>
                    <span class="benefit-badge-label">Rich in<br/>Vitamins</span>
                  </div>
                  <div class="benefit-badge">
                    <div class="benefit-badge-icon">
                      <svg fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
                      </svg>
                    </div>
                    <span class="benefit-badge-label">Good for<br/>Heart</span>
                  </div>
                </div>
              </div>

              <!-- Reviews Card -->
              <div class="reviews-card">
                <div class="quote-icon">“</div>
                <div class="card-title">What Our Customers Say</div>
                <div class="stars">★★★★★</div>
                <p class="testimonial-text" id="review-text">[Placeholder Review 1] "Super fresh products and great variety. Fishcart is our family's choice."</p>
                <div class="attribution" id="review-author">– Priya S.</div>
                <div class="dots-container">
                  <div class="dot active" onclick="switchReview(0)"></div>
                  <div class="dot" onclick="switchReview(1)"></div>
                  <div class="dot" onclick="switchReview(2)"></div>
                </div>
              </div>
            </div>

            <!-- ROW 3: Product Grid -->
            <div class="r3">
              <div class="product-tile" onclick="go('fish')">
                <img alt="Fish" src="assets/fish_showcase.png"/>
                <div class="scrim"></div>
                <div class="tile-content">
                  <span class="tile-label">All Fish Items</span>
                  <span class="tile-link">
                    Explore Now
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </span>
                </div>
              </div>
              <div class="product-tile" onclick="go('meat')">
                <img alt="Meat" src="assets/meat_showcase.png"/>
                <div class="scrim"></div>
                <div class="tile-content">
                  <span class="tile-label">All Meat Items</span>
                  <span class="tile-link">
                    Explore Now
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </span>
                </div>
              </div>
              <div class="product-tile" onclick="go('chicken')">
                <img alt="Chicken" src="assets/chicken_showcase.png"/>
                <div class="scrim"></div>
                <div class="tile-content">
                  <span class="tile-label">Chicken Items</span>
                  <span class="tile-link">
                    Explore Now
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </span>
                </div>
              </div>
              <div class="product-tile" onclick="go('eggs')">
                <img alt="Eggs" src="assets/eggs_showcase.png"/>
                <div class="scrim"></div>
                <div class="tile-content">
                  <span class="tile-label">Eggs</span>
                  <span class="tile-link">
                    Explore Now
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:10px; height:10px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </span>
                </div>
              </div>
            </div>

            <!-- ROW 4: Features -->
            <div class="r4">
              <div class="feature-card freshness">
                <div class="feat-text">
                  <div class="feat-title">Freshness<br/>You Can Trust</div>
                  <div class="feat-desc">We ensure premium quality and freshness in every product we deliver.</div>
                </div>
                <div class="icon-circle">
                  <svg fill="currentColor" viewBox="0 0 24 24" style="width:20px; height:20px;">
                    <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"></path>
                  </svg>
                </div>
              </div>

              <div class="feature-card daily">
                <div class="feat-text">
                  <div class="feat-title">Daily Selection</div>
                  <div class="feat-desc">Handpicked daily from trusted suppliers for the best quality.</div>
                </div>
                <div class="icon-circle">
                  <svg fill="currentColor" viewBox="0 0 24 24" style="width:18px; height:18px;">
                    <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
                  </svg>
                </div>
              </div>

              <div class="feature-card hygienic">
                <div class="feat-text">
                  <div class="feat-title">Hygienic & Safe</div>
                  <div class="feat-desc">Cleaned, packed and delivered with highest hygiene standards.</div>
                </div>
                <div class="icon-circle">
                  <svg fill="currentColor" viewBox="0 0 24 24" style="width:20px; height:20px;">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path>
                  </svg>
                </div>
              </div>

              <div class="feature-card sourced">
                <div class="feat-text">
                  <div class="feat-title">Sourced Responsibly</div>
                  <div class="feat-desc">We care for the ocean and the environment for a better future.</div>
                </div>
                <div class="icon-circle">
                  <svg fill="currentColor" viewBox="0 0 24 24" style="width:20px; height:20px;">
                    <path d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1-2.3A4.49 4.49 0 008 20c4 0 4-2 8-2s4 2 8 2v-2c-4 0-4-2-8-2-1.17 0-1.85.17-2.47.34C14.22 14.5 17.5 12 22 10V8z"></path>
                  </svg>
                </div>
              </div>

              <div class="feature-card community">
                <div class="community-left">
                  <div class="feat-title">Join Our Community</div>
                  <div class="feat-desc" style="font-size:9.5px; opacity:0.85;">Be a part of our journey for healthy and delicious living.</div>
                  <button class="join-btn" onclick="go('about')">
                    Join Us
                    <svg fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="width:8px; height:8px;">
                      <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                  </button>
                </div>
                <div class="qr-container" style="position: relative; width: 62px; height: 62px; background: #fff; border-radius: 10px; padding: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                  <img src="assets/whatsapp_qr.png" alt="WhatsApp QR Code" style="width: 100%; height: 100%; object-fit: contain;" />
                  <div class="wa-badge" style="position: absolute; bottom: -3px; right: -3px; width: 18px; height: 18px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1.5px solid #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.15);">
                    <svg width="10" height="10" fill="#fff" viewBox="0 0 24 24">
                      <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.514 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.733-1.455L0 24zm6.59-4.846c1.6.95 3.188 1.449 4.625 1.451 5.403.002 9.803-4.386 9.805-9.789.002-2.618-1.01-5.08-2.859-6.93C16.328 2.036 13.88 1.023 11.995 1.023c-5.41 0-9.813 4.39-9.815 9.794-.001 1.942.493 3.498 1.424 5.087L2.617 21.605l4.03-1.451zM17.06 14.54c-.274-.138-1.62-.8-1.871-.892-.252-.092-.435-.138-.619.138-.183.276-.708.892-.868 1.077-.16.184-.32.207-.594.069-.273-.138-1.157-.426-2.202-1.358-.813-.726-1.362-1.623-1.522-1.899-.16-.276-.017-.425.12-.562.124-.124.274-.322.412-.483.137-.161.183-.276.274-.459.091-.183.046-.344-.023-.482-.069-.138-.619-1.492-.848-2.043-.224-.54-.469-.465-.643-.474l-.549-.01c-.189 0-.497.07-.757.354-.26.284-.993.97-.993 2.366 0 1.396 1.016 2.748 1.158 2.94.143.19 1.999 3.052 4.842 4.279.676.292 1.204.467 1.616.598.679.216 1.297.185 1.785.112.544-.08 1.62-.662 1.85-1.298.23-.635.23-1.18.162-1.298-.069-.118-.252-.207-.526-.345z"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>

            <!-- ROW 5: Footer -->
            <div class="r5">
              <div class="footer-card">
                <div class="fc-text">
                  <span class="fc-title">About Us</span>
                  <span class="fc-desc">We are passionate about delivering fresh and healthy food to your family.</span>
                </div>
                <div style="flex-shrink:0;">
                  <svg fill="none" style="width:40px;height:22px;" viewBox="0 0 60 30">
                    <path d="M10 15 Q20 8 30 15 T50 15" stroke="#0f46bd" stroke-width="1.5"></path>
                    <ellipse cx="30" cy="15" rx="14" ry="7" stroke="#0f46bd" stroke-width="1.5"></ellipse>
                    <path d="M16 15 L8 10 L8 20 Z" stroke="#0f46bd" stroke-width="1.5"></path>
                    <circle cx="37" cy="13" fill="#0f46bd" r="1.5"></circle>
                  </svg>
                </div>
              </div>

              <div class="footer-card">
                <div class="fc-text">
                  <span class="fc-title">Our Stories</span>
                  <span class="fc-desc">From ocean to your kitchen, our journey of freshness.</span>
                </div>
                <img alt="Our Stories Boat" class="fc-img" src="assets/our_stories_boat.png"/>
              </div>

              <div class="footer-card">
                <div class="fc-text">
                  <span class="fc-title">Contact Us</span>
                  <span class="fc-desc">We are here to help you. Reach out anytime.</span>
                </div>
                <img alt="Contact Boy" class="fc-img" src="assets/contact_boy.png"/>
              </div>

              <div class="footer-card">
                <div class="fc-text" style="gap:4px;">
                  <div class="footer-contact-item">
                    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"></path></svg>
                    <span>Unit 5 Hythe Quay, Colchester, England, CO2 8JB</span>
                  </div>
                  <div class="footer-contact-item">
                    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"></path></svg>
                    <span>+44 1206 123456</span>
                  </div>
                  <div class="footer-contact-item">
                    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"></path></svg>
                    <span>hello@fishcart.co.uk</span>
                  </div>
                </div>
                <div style="flex-shrink:0;">
                  <svg fill="none" style="width:65px;height:24px;" viewBox="0 0 100 30">
                    <path d="M5 15 Q25 8 50 15 Q75 22 95 15" stroke="#0f46bd" stroke-width="1.2"></path>
                    <ellipse cx="75" cy="14" rx="12" ry="6" stroke="#0f46bd" stroke-width="1.2"></ellipse>
                    <path d="M63 14 L57 10 L57 18 Z" stroke="#0f46bd" stroke-width="1.2"></path>
                    <ellipse cx="25" cy="18" rx="8" ry="4" stroke="#0f46bd" stroke-width="1"></ellipse>
                    <path d="M17 18 L12 15 L12 21 Z" stroke="#0f46bd" stroke-width="1"></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>"""
NEW_SCRIPTS = """  <div class="page" id="page-contact"><div class="ph"><div class="ph-ico">📞</div><div class="ph-title">Contact Us</div><div class="ph-sub">Send me the reference — ready to build!</div></div></div>
  </main>
  </div>
  </div>
  <script>
    const reviews = [
        {
            text: "[Placeholder Review 1] Super fresh products and great variety. Fishcart is our family's choice.",
            author: '– Priya S.'
        },
        {
            text: "[Placeholder Review 2] Outstanding quality! The meat was perfectly packed and delivered cold.",
            author: '– John D.'
        },
        {
            text: "[Placeholder Review 3] The best eggs and fresh fish in town. Highly recommend their daily catch.",
            author: '– Server M.'
        }
    ];

    function switchReview(index) {
        const textEl = document.getElementById('review-text');
        const authorEl = document.getElementById('review-author');
        if (textEl && authorEl) {
            textEl.innerText = reviews[index].text;
            authorEl.innerText = reviews[index].author;
        }
        const dots = document.querySelectorAll('.reviews-card .dot');
        dots.forEach((dot, idx) => {
            if (idx === index) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    function go(id) {
      document.querySelectorAll('.ni').forEach(el => el.classList.remove('active'));
      const n = document.getElementById('nav-' + id);
      if (n) n.classList.add('active');
      document.querySelectorAll('.page').forEach(el => el.classList.remove('active'));
      const p = document.getElementById('page-' + id);
      if (p) p.classList.add('active');
    }

    window.addEventListener('load', () => {
      if (window.location.hash) {
        const hashId = window.location.hash.substring(1);
        if (document.getElementById('page-' + hashId)) {
          go(hashId);
        }
      }
    });

    /* ── VIEWPORT FIT SCALER ── */
    function fitApp() {
      var app = document.querySelector('.app');
      if (!app) return;
      var appW = 1448;
      var appH = 1086;
      var vw = window.innerWidth;
      var vh = window.innerHeight;
      var scale = Math.min(vw / appW, vh / appH);
      var scaledW = appW * scale;
      var scaledH = appH * scale;
      var left = Math.round((vw - scaledW) / 2);
      var top = Math.round((vh - scaledH) / 2);
      app.style.transform = 'scale(' + scale + ')';
      app.style.left = left + 'px';
      app.style.top = top + 'px';
    }
    window.addEventListener('resize', fitApp);
    window.addEventListener('orientationchange', fitApp);
    fitApp();
  </script>"""

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace styles
# We search for the open and close markers of the style section
style_start = content.find('<link href="https://fonts.googleapis.com" rel="preconnect"/>')
style_end = content.find('</style>', style_start)
if style_start == -1 or style_end == -1:
    print("Could not find style block markers")
    sys.exit(1)

content_styles_patched = content[:style_start] + NEW_STYLES + content[style_end + len('</style>'):]

# Replace body/home section
# Target starts at <body> and ends before <!-- ═══ OTHER PAGES -->
body_start = content_styles_patched.find('<body>')
other_pages_start = content_styles_patched.find('<!-- ═══ OTHER PAGES (placeholders until you guide me) ═══ -->')
if body_start == -1 or other_pages_start == -1:
    print("Could not find body or other pages start markers")
    sys.exit(1)

content_body_patched = content_styles_patched[:body_start] + NEW_BODY + '\n' + content_styles_patched[other_pages_start:]

# Remove early closing </div> of div.app that is right before page-cook (line 1376 in clean file)
# The markers are <!-- CONTACT US MODAL --> and <!-- ═══ COOK PAGE ═══ -->
# Let's search for <!-- CONTACT US MODAL -->\n</div>\n<!-- ═══ COOK PAGE ═══ --> or with CRLF
target_early_close = "<!-- CONTACT US MODAL -->\n</div>\n<!-- ═══ COOK PAGE ═══ -->"
target_early_close_crlf = "<!-- CONTACT US MODAL -->\r\n</div>\r\n<!-- ═══ COOK PAGE ═══ -->"

if target_early_close in content_body_patched:
    content_body_patched = content_body_patched.replace(target_early_close, "<!-- CONTACT US MODAL -->\n<!-- ═══ COOK PAGE ═══ -->")
    print("Removed early closing div tag (LF format)")
elif target_early_close_crlf in content_body_patched:
    content_body_patched = content_body_patched.replace(target_early_close_crlf, "<!-- CONTACT US MODAL -->\r\n<!-- ═══ COOK PAGE ═══ -->")
    print("Removed early closing div tag (CRLF format)")
else:
    # Let's fall back to searching for </div>\n<!-- ═══ COOK PAGE ═══ -->
    fallback = "</div>\n<!-- ═══ COOK PAGE ═══ -->"
    fallback_crlf = "</div>\r\n<!-- ═══ COOK PAGE ═══ -->"
    if fallback in content_body_patched:
        content_body_patched = content_body_patched.replace(fallback, "<!-- ═══ COOK PAGE ═══ -->")
        print("Removed early closing div tag (fallback LF)")
    elif fallback_crlf in content_body_patched:
        content_body_patched = content_body_patched.replace(fallback_crlf, "<!-- ═══ COOK PAGE ═══ -->")
        print("Removed early closing div tag (fallback CRLF)")
    else:
        print("Warning: Could not find early closing div tag right before COOK PAGE")

# Replace scripts section at bottom
# Target starts at page-contact and ends at the closing </script> right before const pdData
# Let's search for page-contact and the <script> following it
contact_idx = content_body_patched.find('<div class="page" id="page-contact">')
if contact_idx == -1:
    print("Could not find page-contact in content")
    sys.exit(1)

script_start = content_body_patched.find('<script>', contact_idx)
script_end = content_body_patched.find('</script>', script_start)
if script_start == -1 or script_end == -1:
    print("Could not find scripts block at bottom")
    sys.exit(1)

final_content = content_body_patched[:contact_idx] + NEW_SCRIPTS + content_body_patched[script_end + len('</script>'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Successfully overhauled index.html layout!")
