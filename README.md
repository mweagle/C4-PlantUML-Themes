# C4-PlantUML-Themes

C4-PlantUML-Themes autogenerated from ColorBrewer and Seaborn palettes. See the C4-Plant UML [Themes](https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/Themes.md) page for more information on the variables set by each theme.

Usage:

```

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' START - Handle local PlantUML render and remote hosting
'
!$THEME_NAME = div_RdGy_9
'
!if (%getenv("LOCAL_EDIT_BLOG_ROOT") == "")
!$THEME_ROOT_PATH = "https://YOUR_HOSTNAME/resources/"
!else
!$THEME_ROOT_PATH = %getenv("LOCAL_EDIT_BLOG_ROOT") + "/resources/"
!endif
!define INCLUDE(a,b) ##a##b

' Define the theme name we're going to use
!if (%getenv("LOCAL_EDIT_BLOG_ROOT") == "")
!theme $THEME_NAME from https://YOUR_HOSTNAME/resources/palettes
!else
!theme $THEME_NAME from resources/palettes
!endif

!include INCLUDE($THEME_ROOT_PATH, c4-theme-common.puml)
' END - Handle local PlantUML render and remote hosting
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
```

where _c4-theme-common.puml_ is as follows (depends on [PlantUML PR 295](https://github.com/plantuml-stdlib/C4-PlantUML/pull/295) or later):

```
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4.puml)
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4_Component.puml)
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4_Container.puml)
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4_Context.puml)
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4_Deployment.puml)
!include INCLUDE($THEME_ROOT_PATH, C4-PlantUML/C4_Dynamic.puml)

skinparam DefaultFontName Open Sans
skinparam Handwritten false
skinparam TitleFontSize 24
```


The generated theme files are below:

## puml-theme-cb_div_RdGy_11.puml

[![./palettes/puml-theme-cb_div_RdGy_11.png](./palettes/puml-theme-cb_div_RdGy_11.png)](./palettes/puml-theme-cb_div_RdGy_11.puml)

## puml-theme-seaborn_Dark2_9.puml

[![./palettes/puml-theme-seaborn_Dark2_9.png](./palettes/puml-theme-seaborn_Dark2_9.png)](./palettes/puml-theme-seaborn_Dark2_9.puml)

## puml-theme-cb_seq_Purples_9.puml

[![./palettes/puml-theme-cb_seq_Purples_9.png](./palettes/puml-theme-cb_seq_Purples_9.png)](./palettes/puml-theme-cb_seq_Purples_9.puml)

## puml-theme-cb_div_RdYlBu_11.puml

[![./palettes/puml-theme-cb_div_RdYlBu_11.png](./palettes/puml-theme-cb_div_RdYlBu_11.png)](./palettes/puml-theme-cb_div_RdYlBu_11.puml)

## puml-theme-seaborn_crest_9.puml

[![./palettes/puml-theme-seaborn_crest_9.png](./palettes/puml-theme-seaborn_crest_9.png)](./palettes/puml-theme-seaborn_crest_9.puml)

## puml-theme-cb_div_PuOr_9.puml

[![./palettes/puml-theme-cb_div_PuOr_9.png](./palettes/puml-theme-cb_div_PuOr_9.png)](./palettes/puml-theme-cb_div_PuOr_9.puml)

## puml-theme-seaborn_Pastel2_9.puml

[![./palettes/puml-theme-seaborn_Pastel2_9.png](./palettes/puml-theme-seaborn_Pastel2_9.png)](./palettes/puml-theme-seaborn_Pastel2_9.puml)

## puml-theme-seaborn_Set1_9.puml

[![./palettes/puml-theme-seaborn_Set1_9.png](./palettes/puml-theme-seaborn_Set1_9.png)](./palettes/puml-theme-seaborn_Set1_9.puml)

## puml-theme-seaborn_flare_9.puml

[![./palettes/puml-theme-seaborn_flare_9.png](./palettes/puml-theme-seaborn_flare_9.png)](./palettes/puml-theme-seaborn_flare_9.puml)

## puml-theme-seaborn_husl_9.puml

[![./palettes/puml-theme-seaborn_husl_9.png](./palettes/puml-theme-seaborn_husl_9.png)](./palettes/puml-theme-seaborn_husl_9.puml)

## puml-theme-cb_div_PiYG_11.puml

[![./palettes/puml-theme-cb_div_PiYG_11.png](./palettes/puml-theme-cb_div_PiYG_11.png)](./palettes/puml-theme-cb_div_PiYG_11.puml)

## puml-theme-cb_seq_GnBu_9.puml

[![./palettes/puml-theme-cb_seq_GnBu_9.png](./palettes/puml-theme-cb_seq_GnBu_9.png)](./palettes/puml-theme-cb_seq_GnBu_9.puml)

## puml-theme-seaborn_vlag_9.puml

[![./palettes/puml-theme-seaborn_vlag_9.png](./palettes/puml-theme-seaborn_vlag_9.png)](./palettes/puml-theme-seaborn_vlag_9.puml)

## puml-theme-seaborn_Set3_9.puml

[![./palettes/puml-theme-seaborn_Set3_9.png](./palettes/puml-theme-seaborn_Set3_9.png)](./palettes/puml-theme-seaborn_Set3_9.puml)

## puml-theme-cb_qual_Paired_9.puml

[![./palettes/puml-theme-cb_qual_Paired_9.png](./palettes/puml-theme-cb_qual_Paired_9.png)](./palettes/puml-theme-cb_qual_Paired_9.puml)

## puml-theme-cb_div_PRGn_9.puml

[![./palettes/puml-theme-cb_div_PRGn_9.png](./palettes/puml-theme-cb_div_PRGn_9.png)](./palettes/puml-theme-cb_div_PRGn_9.puml)

## puml-theme-cb_div_PuOr_11.puml

[![./palettes/puml-theme-cb_div_PuOr_11.png](./palettes/puml-theme-cb_div_PuOr_11.png)](./palettes/puml-theme-cb_div_PuOr_11.puml)

## puml-theme-cb_div_RdBu_11.puml

[![./palettes/puml-theme-cb_div_RdBu_11.png](./palettes/puml-theme-cb_div_RdBu_11.png)](./palettes/puml-theme-cb_div_RdBu_11.puml)

## puml-theme-cb_div_PiYG_9.puml

[![./palettes/puml-theme-cb_div_PiYG_9.png](./palettes/puml-theme-cb_div_PiYG_9.png)](./palettes/puml-theme-cb_div_PiYG_9.puml)

## puml-theme-cb_div_BrBG_9.puml

[![./palettes/puml-theme-cb_div_BrBG_9.png](./palettes/puml-theme-cb_div_BrBG_9.png)](./palettes/puml-theme-cb_div_BrBG_9.puml)

## puml-theme-cb_qual_Set3_9.puml

[![./palettes/puml-theme-cb_qual_Set3_9.png](./palettes/puml-theme-cb_qual_Set3_9.png)](./palettes/puml-theme-cb_qual_Set3_9.puml)

## puml-theme-cb_seq_PuBuGn_9.puml

[![./palettes/puml-theme-cb_seq_PuBuGn_9.png](./palettes/puml-theme-cb_seq_PuBuGn_9.png)](./palettes/puml-theme-cb_seq_PuBuGn_9.puml)

## puml-theme-cb_seq_BuGn_9.puml

[![./palettes/puml-theme-cb_seq_BuGn_9.png](./palettes/puml-theme-cb_seq_BuGn_9.png)](./palettes/puml-theme-cb_seq_BuGn_9.puml)

## puml-theme-seaborn_icefire_9.puml

[![./palettes/puml-theme-seaborn_icefire_9.png](./palettes/puml-theme-seaborn_icefire_9.png)](./palettes/puml-theme-seaborn_icefire_9.puml)

## puml-theme-cb_div_RdYlGn_11.puml

[![./palettes/puml-theme-cb_div_RdYlGn_11.png](./palettes/puml-theme-cb_div_RdYlGn_11.png)](./palettes/puml-theme-cb_div_RdYlGn_11.puml)

## puml-theme-cb_qual_Pastel1_9.puml

[![./palettes/puml-theme-cb_qual_Pastel1_9.png](./palettes/puml-theme-cb_qual_Pastel1_9.png)](./palettes/puml-theme-cb_qual_Pastel1_9.puml)

## puml-theme-cb_seq_OrRd_9.puml

[![./palettes/puml-theme-cb_seq_OrRd_9.png](./palettes/puml-theme-cb_seq_OrRd_9.png)](./palettes/puml-theme-cb_seq_OrRd_9.puml)

## puml-theme-cb_div_RdBu_9.puml

[![./palettes/puml-theme-cb_div_RdBu_9.png](./palettes/puml-theme-cb_div_RdBu_9.png)](./palettes/puml-theme-cb_div_RdBu_9.puml)

## puml-theme-cb_qual_Set1_9.puml

[![./palettes/puml-theme-cb_qual_Set1_9.png](./palettes/puml-theme-cb_qual_Set1_9.png)](./palettes/puml-theme-cb_qual_Set1_9.puml)

## puml-theme-cb_qual_Set3_11.puml

[![./palettes/puml-theme-cb_qual_Set3_11.png](./palettes/puml-theme-cb_qual_Set3_11.png)](./palettes/puml-theme-cb_qual_Set3_11.puml)

## puml-theme-cb_seq_PuRd_9.puml

[![./palettes/puml-theme-cb_seq_PuRd_9.png](./palettes/puml-theme-cb_seq_PuRd_9.png)](./palettes/puml-theme-cb_seq_PuRd_9.puml)

## puml-theme-cb_seq_PuBu_9.puml

[![./palettes/puml-theme-cb_seq_PuBu_9.png](./palettes/puml-theme-cb_seq_PuBu_9.png)](./palettes/puml-theme-cb_seq_PuBu_9.puml)

## puml-theme-cb_seq_Blues_9.puml

[![./palettes/puml-theme-cb_seq_Blues_9.png](./palettes/puml-theme-cb_seq_Blues_9.png)](./palettes/puml-theme-cb_seq_Blues_9.puml)

## puml-theme-cb_seq_YlGnBu_9.puml

[![./palettes/puml-theme-cb_seq_YlGnBu_9.png](./palettes/puml-theme-cb_seq_YlGnBu_9.png)](./palettes/puml-theme-cb_seq_YlGnBu_9.puml)

## puml-theme-seaborn_magma_9.puml

[![./palettes/puml-theme-seaborn_magma_9.png](./palettes/puml-theme-seaborn_magma_9.png)](./palettes/puml-theme-seaborn_magma_9.puml)

## puml-theme-cb_div_Spectral_9.puml

[![./palettes/puml-theme-cb_div_Spectral_9.png](./palettes/puml-theme-cb_div_Spectral_9.png)](./palettes/puml-theme-cb_div_Spectral_9.puml)

## puml-theme-cb_seq_BuPu_9.puml

[![./palettes/puml-theme-cb_seq_BuPu_9.png](./palettes/puml-theme-cb_seq_BuPu_9.png)](./palettes/puml-theme-cb_seq_BuPu_9.puml)

## puml-theme-cb_qual_Paired_11.puml

[![./palettes/puml-theme-cb_qual_Paired_11.png](./palettes/puml-theme-cb_qual_Paired_11.png)](./palettes/puml-theme-cb_qual_Paired_11.puml)

## puml-theme-seaborn_deep_9.puml

[![./palettes/puml-theme-seaborn_deep_9.png](./palettes/puml-theme-seaborn_deep_9.png)](./palettes/puml-theme-seaborn_deep_9.puml)

## puml-theme-seaborn_Paired_9.puml

[![./palettes/puml-theme-seaborn_Paired_9.png](./palettes/puml-theme-seaborn_Paired_9.png)](./palettes/puml-theme-seaborn_Paired_9.puml)

## puml-theme-cb_seq_Greys_9.puml

[![./palettes/puml-theme-cb_seq_Greys_9.png](./palettes/puml-theme-cb_seq_Greys_9.png)](./palettes/puml-theme-cb_seq_Greys_9.puml)

## puml-theme-cb_div_BrBG_11.puml

[![./palettes/puml-theme-cb_div_BrBG_11.png](./palettes/puml-theme-cb_div_BrBG_11.png)](./palettes/puml-theme-cb_div_BrBG_11.puml)

## puml-theme-cb_seq_RdPu_9.puml

[![./palettes/puml-theme-cb_seq_RdPu_9.png](./palettes/puml-theme-cb_seq_RdPu_9.png)](./palettes/puml-theme-cb_seq_RdPu_9.puml)

## puml-theme-cb_div_RdGy_9.puml

[![./palettes/puml-theme-cb_div_RdGy_9.png](./palettes/puml-theme-cb_div_RdGy_9.png)](./palettes/puml-theme-cb_div_RdGy_9.puml)

## puml-theme-cb_div_RdYlBu_9.puml

[![./palettes/puml-theme-cb_div_RdYlBu_9.png](./palettes/puml-theme-cb_div_RdYlBu_9.png)](./palettes/puml-theme-cb_div_RdYlBu_9.puml)

## puml-theme-seaborn_mako_9.puml

[![./palettes/puml-theme-seaborn_mako_9.png](./palettes/puml-theme-seaborn_mako_9.png)](./palettes/puml-theme-seaborn_mako_9.puml)

## puml-theme-seaborn_Pastel1_9.puml

[![./palettes/puml-theme-seaborn_Pastel1_9.png](./palettes/puml-theme-seaborn_Pastel1_9.png)](./palettes/puml-theme-seaborn_Pastel1_9.puml)

## puml-theme-seaborn_Set2_9.puml

[![./palettes/puml-theme-seaborn_Set2_9.png](./palettes/puml-theme-seaborn_Set2_9.png)](./palettes/puml-theme-seaborn_Set2_9.puml)

## puml-theme-cb_seq_YlOrBr_9.puml

[![./palettes/puml-theme-cb_seq_YlOrBr_9.png](./palettes/puml-theme-cb_seq_YlOrBr_9.png)](./palettes/puml-theme-cb_seq_YlOrBr_9.puml)

## puml-theme-seaborn_Accent_9.puml

[![./palettes/puml-theme-seaborn_Accent_9.png](./palettes/puml-theme-seaborn_Accent_9.png)](./palettes/puml-theme-seaborn_Accent_9.puml)

## puml-theme-cb_seq_YlGn_9.puml

[![./palettes/puml-theme-cb_seq_YlGn_9.png](./palettes/puml-theme-cb_seq_YlGn_9.png)](./palettes/puml-theme-cb_seq_YlGn_9.puml)

## puml-theme-cb_seq_Oranges_9.puml

[![./palettes/puml-theme-cb_seq_Oranges_9.png](./palettes/puml-theme-cb_seq_Oranges_9.png)](./palettes/puml-theme-cb_seq_Oranges_9.puml)

## puml-theme-cb_div_Spectral_11.puml

[![./palettes/puml-theme-cb_div_Spectral_11.png](./palettes/puml-theme-cb_div_Spectral_11.png)](./palettes/puml-theme-cb_div_Spectral_11.puml)

## puml-theme-seaborn_viridis_9.puml

[![./palettes/puml-theme-seaborn_viridis_9.png](./palettes/puml-theme-seaborn_viridis_9.png)](./palettes/puml-theme-seaborn_viridis_9.puml)

## puml-theme-seaborn_gray_9.puml

[![./palettes/puml-theme-seaborn_gray_9.png](./palettes/puml-theme-seaborn_gray_9.png)](./palettes/puml-theme-seaborn_gray_9.puml)

## puml-theme-cb_seq_Greens_9.puml

[![./palettes/puml-theme-cb_seq_Greens_9.png](./palettes/puml-theme-cb_seq_Greens_9.png)](./palettes/puml-theme-cb_seq_Greens_9.puml)

## puml-theme-cb_div_PRGn_11.puml

[![./palettes/puml-theme-cb_div_PRGn_11.png](./palettes/puml-theme-cb_div_PRGn_11.png)](./palettes/puml-theme-cb_div_PRGn_11.puml)

## puml-theme-seaborn_rocket_9.puml

[![./palettes/puml-theme-seaborn_rocket_9.png](./palettes/puml-theme-seaborn_rocket_9.png)](./palettes/puml-theme-seaborn_rocket_9.puml)

## puml-theme-cb_seq_Reds_9.puml

[![./palettes/puml-theme-cb_seq_Reds_9.png](./palettes/puml-theme-cb_seq_Reds_9.png)](./palettes/puml-theme-cb_seq_Reds_9.puml)

## puml-theme-cb_div_RdYlGn_9.puml

[![./palettes/puml-theme-cb_div_RdYlGn_9.png](./palettes/puml-theme-cb_div_RdYlGn_9.png)](./palettes/puml-theme-cb_div_RdYlGn_9.puml)
