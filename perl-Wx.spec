%define upstream_name Wx
%define upstream_version 0.98

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Interface to the wxWidgets GUI toolkit
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Alien::wxWidgets)
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.220.600
BuildRequires:	perl(ExtUtils::XSpp)
BuildRequires:	wxgtku2.8-devel
BuildRequires:	perl-devel

# Olivier Thauvin
# https://qa.mandriva.com/show_bug.cgi?id=43053
# This hudge list come from all XS
# find req/prov are unable at time to list XS package :\
Provides:	perl(Wx::AcceleratorEntry)
Provides:	perl(Wx::AcceleratorTable)
Provides:	perl(Wx::ActivateEvent)
Provides:	perl(Wx::ANIHandler)
Provides:	perl(Wx::App)
Provides:	perl(Wx::_App)
Provides:	perl(Wx::ArchiveFSHandler)
Provides:	perl(Wx::AUI)
Provides:	perl(Wx::BestHelpController)
Provides:	perl(Wx::Bitmap)
Provides:	perl(Wx::BitmapButton)
Provides:	perl(Wx::BitmapDataObject)
Provides:	perl(Wx::BitmapToggleButton)
Provides:	perl(Wx::BMPHandler)
Provides:	perl(Wx::BoxSizer)
Provides:	perl(Wx::Brush)
Provides:	perl(Wx::BusyCursor)
Provides:	perl(Wx::BusyInfo)
Provides:	perl(Wx::Button)
Provides:	perl(Wx::Caret)
Provides:	perl(Wx::CaretSuspend)
Provides:	perl(Wx::CheckBox)
Provides:	perl(Wx::CheckListBox)
Provides:	perl(Wx::ChildFocusEvent)
Provides:	perl(Wx::CHMHelpController)
Provides:	perl(Wx::Choice)
Provides:	perl(Wx::ClassInfo)
Provides:	perl(Wx::ClientDC)
Provides:	perl(Wx::Clipboard)
Provides:	perl(Wx::ClipboardTextEvent)
Provides:	perl(Wx::CloseEvent)
Provides:	perl(Wx::Colour)
Provides:	perl(Wx::ColourData)
Provides:	perl(Wx::ColourDatabase)
Provides:	perl(Wx::ColourDialog)
Provides:	perl(Wx::ComboBox)
Provides:	perl(Wx::CommandEvent)
Provides:	perl(Wx::ConfigBase)
Provides:	perl(Wx::ContextHelp)
Provides:	perl(Wx::ContextHelpButton)
Provides:	perl(Wx::ContextMenuEvent)
Provides:	perl(Wx::Control)
Provides:	perl(Wx::CURHandler)
Provides:	perl(Wx::Cursor)
Provides:	perl(Wx::DataFormat)
Provides:	perl(Wx::DataObject)
Provides:	perl(Wx::DataObjectComposite)
Provides:	perl(Wx::DataObjectSimple)
Provides:	perl(Wx::DataView)
Provides:	perl(Wx::DC)
Provides:	perl(Wx::Dialog)
Provides:	perl(Wx::DirDialog)
Provides:	perl(Wx::DocChildFrame)
Provides:	perl(Wx::DocManager)
Provides:	perl(Wx::DocMDIChildFrame)
Provides:	perl(Wx::DocMDIParentFrame)
Provides:	perl(Wx::DocParentFrame)
Provides:	perl(Wx::DocTemplate)
Provides:	perl(Wx::Document)
Provides:	perl(Wx::DropFilesEvent)
Provides:	perl(Wx::DropSource)
Provides:	perl(Wx::DropTarget)
Provides:	perl(Wx::EraseEvent)
Provides:	perl(Wx::Event)
Provides:	perl(Wx::EvtHandler)
Provides:	perl(Wx::FileConfig)
Provides:	perl(Wx::FileDataObject)
Provides:	perl(Wx::FileDialog)
Provides:	perl(Wx::FileDropTarget)
Provides:	perl(Wx::FileHistory)
Provides:	perl(Wx::FileSystem)
Provides:	perl(Wx::FileSystemHandler)
Provides:	perl(Wx::FindDialogEvent)
Provides:	perl(Wx::FindReplaceData)
Provides:	perl(Wx::FindReplaceDialog)
Provides:	perl(Wx::FlexGridSizer)
Provides:	perl(Wx::FocusEvent)
Provides:	perl(Wx::Font)
Provides:	perl(Wx::FontData)
Provides:	perl(Wx::FontDialog)
Provides:	perl(Wx::FontEnumerator)
Provides:	perl(Wx::FontMapper)
Provides:	perl(Wx::Frame)
Provides:	perl(Wx::FSFile)
Provides:	perl(Wx::Gauge)
Provides:	perl(Wx::GIFHandler)
Provides:	perl(Wx::GraphicsBrush)
Provides:	perl(Wx::GraphicsContext)
Provides:	perl(Wx::GraphicsFont)
Provides:	perl(Wx::GraphicsMatrix)
Provides:	perl(Wx::GraphicsObject)
Provides:	perl(Wx::GraphicsPath)
Provides:	perl(Wx::GraphicsPen)
Provides:	perl(Wx::Grid)
Provides:	perl(Wx::GridCellAttr)
Provides:	perl(Wx::GridCellAutoWrapStringEditor)
Provides:	perl(Wx::GridCellAutoWrapStringRenderer)
Provides:	perl(Wx::GridCellBoolEditor)
Provides:	perl(Wx::GridCellBoolRenderer)
Provides:	perl(Wx::GridCellChoiceEditor)
Provides:	perl(Wx::GridCellCoords)
Provides:	perl(Wx::GridCellDateTimeRenderer)
Provides:	perl(Wx::GridCellEditor)
Provides:	perl(Wx::GridCellEnumEditor)
Provides:	perl(Wx::GridCellEnumRenderer)
Provides:	perl(Wx::GridCellFloatEditor)
Provides:	perl(Wx::GridCellFloatRenderer)
Provides:	perl(Wx::GridCellNumberEditor)
Provides:	perl(Wx::GridCellNumberRenderer)
Provides:	perl(Wx::GridCellRenderer)
Provides:	perl(Wx::GridCellStringRenderer)
Provides:	perl(Wx::GridCellTextEditor)
Provides:	perl(Wx::GridEditorCreatedEvent)
Provides:	perl(Wx::GridEvent)
Provides:	perl(Wx::GridRangeSelectEvent)
Provides:	perl(Wx::GridSizeEvent)
Provides:	perl(Wx::GridSizer)
Provides:	perl(Wx::GridUpdateLocker)
Provides:	perl(Wx::HeaderCtrlSimple)
Provides:	perl(Wx::HelpControllerBase)
Provides:	perl(Wx::HelpControllerHelpProvider)
Provides:	perl(Wx::HelpEvent)
Provides:	perl(Wx::HelpProvider)
Provides:	perl(Wx::HtmlDCRenderer)
Provides:	perl(Wx::HtmlEasyPrinting)
Provides:	perl(Wx::HtmlHelpController)
Provides:	perl(Wx::HtmlLinkInfo)
Provides:	perl(Wx::HtmlWindow)
Provides:	perl(Wx::ICOHandler)
Provides:	perl(Wx::Icon)
Provides:	perl(Wx::IconizeEvent)
Provides:	perl(Wx::IdleEvent)
Provides:	perl(Wx::IFFHandler)
Provides:	perl(Wx::Image)
Provides:	perl(Wx::ImageHandler)
Provides:	perl(Wx::ImageList)
Provides:	perl(Wx::IndividualLayoutConstraint)
Provides:	perl(Wx::InitDialogEvent)
Provides:	perl(Wx::InputStream)
Provides:	perl(Wx::InternetFSHandler)
Provides:	perl(Wx::JoystickEvent)
Provides:	perl(Wx::JPEGHandler)
Provides:	perl(Wx::KeyEvent)
Provides:	perl(Wx::LanguageInfo)
Provides:	perl(Wx::LayoutConstraints)
Provides:	perl(Wx::ListBox)
Provides:	perl(Wx::ListCtrl)
Provides:	perl(Wx::ListEvent)
Provides:	perl(Wx::ListItem)
Provides:	perl(Wx::ListItemAttr)
Provides:	perl(Wx::ListView)
Provides:	perl(Wx::Locale)
Provides:	perl(Wx::Log)
Provides:	perl(Wx::LogChain)
Provides:	perl(Wx::LogGui)
Provides:	perl(Wx::LogNull)
Provides:	perl(Wx::LogPassThrough)
Provides:	perl(Wx::LogStderr)
Provides:	perl(Wx::LogTextCtrl)
Provides:	perl(Wx::LogWindow)
Provides:	perl(Wx::Mask)
Provides:	perl(Wx::MaximizeEvent)
Provides:	perl(Wx::MDIChildFrame)
Provides:	perl(Wx::MDIParentFrame)
Provides:	perl(Wx::Media)
Provides:	perl(Wx::MemoryDC)
Provides:	perl(Wx::MemoryFSHandler)
Provides:	perl(Wx::Menu)
Provides:	perl(Wx::MenuBar)
Provides:	perl(Wx::MenuEvent)
Provides:	perl(Wx::MenuItem)
Provides:	perl(Wx::MiniFrame)
Provides:	perl(Wx::MouseCaptureChangedEvent)
Provides:	perl(Wx::MouseCaptureLostEvent)
Provides:	perl(Wx::MouseEvent)
Provides:	perl(Wx::MoveEvent)
Provides:	perl(Wx::MultiChoiceDialog)
Provides:	perl(Wx::NativeFontInfo)
Provides:	perl(Wx::NavigationKeyEvent)
Provides:	perl(Wx::Notebook)
Provides:	perl(Wx::NotebookEvent)
Provides:	perl(Wx::NotebookSizer)
Provides:	perl(Wx::NotifyEvent)
Provides:	perl(Wx::NumberEntryDialog)
Provides:	perl(Wx::OutputStream)
Provides:	perl(Wx::PageSetupDialog)
Provides:	perl(Wx::PageSetupDialogData)
Provides:	perl(Wx::PaintDC)
Provides:	perl(Wx::PaintEvent)
Provides:	perl(Wx::Palette)
Provides:	perl(Wx::Panel)
Provides:	perl(Wx::PasswordEntryDialog)
Provides:	perl(Wx::PCXHandler)
Provides:	perl(Wx::Pen)
Provides:	perl(Wx::PlComboPopup)
Provides:	perl(Wx::PlCommandEvent)
Provides:	perl(Wx::PlDataObjectSimple)
Provides:	perl(Wx::PlEvent)
Provides:	perl(Wx::PlFileSystemHandler)
Provides:	perl(Wx::PlGridCellEditor)
Provides:	perl(Wx::PlGridCellRenderer)
Provides:	perl(Wx::PlHVScrolledWindow)
Provides:	perl(Wx::PlLog)
Provides:	perl(Wx::PlLogPassThrough)
Provides:	perl(Wx::PlPopupTransientWindow)
Provides:	perl(Wx::PlSizer)
Provides:	perl(Wx::PlThreadEvent)
Provides:	perl(Wx::PlValidator)
Provides:	perl(Wx::PlVListBox)
Provides:	perl(Wx::PlVScrolledWindow)
Provides:	perl(Wx::PNGHandler)
Provides:	perl(Wx::PNMHandler)
Provides:	perl(Wx::Point)
Provides:	perl(Wx::PopupWindow)
Provides:	perl(Wx::Position)
Provides:	perl(Wx::PreviewCanvas)
Provides:	perl(Wx::PrintData)
Provides:	perl(Wx::PrintDialog)
Provides:	perl(Wx::PrintDialogData)
Provides:	perl(Wx::Printer)
Provides:	perl(Wx::PrinterDC)
Provides:	perl(Wx::Printout)
Provides:	perl(Wx::PrintPreview)
Provides:	perl(Wx::Process)
Provides:	perl(Wx::ProcessEvent)
Provides:	perl(Wx::ProgressDialog)
Provides:	perl(Wx::RadioBox)
Provides:	perl(Wx::RadioButton)
Provides:	perl(Wx::Rect)
Provides:	perl(Wx::RegConfig)
Provides:	perl(Wx::Region)
Provides:	perl(Wx::RichText)
Provides:	perl(Wx::SashEvent)
Provides:	perl(Wx::SashWindow)
Provides:	perl(Wx::ScreenDC)
Provides:	perl(Wx::ScrollBar)
Provides:	perl(Wx::ScrolledWindow)
Provides:	perl(Wx::ScrollEvent)
Provides:	perl(Wx::ScrollWinEvent)
Provides:	perl(Wx::SetCursorEvent)
Provides:	perl(Wx::SimpleHelpProvider)
Provides:	perl(Wx::SingleChoiceDialog)
Provides:	perl(Wx::SingleInstanceChecker)
Provides:	perl(Wx::Size)
Provides:	perl(Wx::SizeEvent)
Provides:	perl(Wx::Sizer)
Provides:	perl(Wx::SizerItem)
Provides:	perl(Wx::Slider)
Provides:	perl(Wx::SocketBase)
Provides:	perl(Wx::SocketClient)
Provides:	perl(Wx::SocketEvent)
Provides:	perl(Wx::SocketServer)
Provides:	perl(Wx::SpinButton)
Provides:	perl(Wx::SpinCtrl)
Provides:	perl(Wx::SpinEvent)
Provides:	perl(Wx::SplashScreen)
Provides:	perl(Wx::SplitterWindow)
Provides:	perl(Wx::StaticBitmap)
Provides:	perl(Wx::StaticBox)
Provides:	perl(Wx::StaticBoxSizer)
Provides:	perl(Wx::StaticLine)
Provides:	perl(Wx::StaticText)
Provides:	perl(Wx::StatusBar)
Provides:	perl(Wx::StopWatch)
Provides:	perl(Wx::Stream)
Provides:	perl(Wx::SysColourChangedEvent)
Provides:	perl(Wx::SystemOptions)
Provides:	perl(Wx::SystemSettings)
Provides:	perl(Wx::TaskBarIcon)
Provides:	perl(Wx::TaskBarIconEvent)
Provides:	perl(Wx::TextDataObject)
Provides:	perl(Wx::TextDropTarget)
Provides:	perl(Wx::TextEntryDialog)
Provides:	perl(Wx::TGAHandler)
Provides:	perl(Wx::Thread)
Provides:	perl(Wx::TIFFHandler)
Provides:	perl(Wx::Timer)
Provides:	perl(Wx::TimerEvent)
Provides:	perl(Wx::TipProvider)
Provides:	perl(Wx::ToggleButton)
Provides:	perl(Wx::ToolBar)
Provides:	perl(Wx::ToolBarBase)
Provides:	perl(Wx::ToolBarToolBase)
Provides:	perl(Wx::ToolTip)
Provides:	perl(Wx::TreeCtrl)
Provides:	perl(Wx::TreeEvent)
Provides:	perl(Wx::TreeItemData)
Provides:	perl(Wx::TreeItemId)
Provides:	perl(Wx::UpdateUIEvent)
Provides:	perl(Wx::URLDataObject)
Provides:	perl(Wx::Validator)
Provides:	perl(Wx::View)
Provides:	perl(Wx::Wave)
Provides:	perl(Wx::Window)
Provides:	perl(Wx::WindowCreateEvent)
Provides:	perl(Wx::WindowDC)
Provides:	perl(Wx::WindowDestroyEvent)
Provides:	perl(Wx::WindowDisabler)
Provides:	perl(Wx::WinHelpController)
Provides:	perl(Wx::Wizard)
Provides:	perl(Wx::WizardEvent)
Provides:	perl(Wx::WizardPage)
Provides:	perl(Wx::WizardPageSimple)
Provides:	perl(Wx::XmlResource)
Provides:	perl(Wx::XPMHandler)
Provides:	perl(Wx::ZipFSHandler)

%description
The Wx module is a wrapper for the wxWidgets (formerly known as wxWindows)
GUI toolkit.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc Changes README.txt
%{perl_vendorarch}/Wx.pm
%{perl_vendorarch}/Wx
%{perl_vendorarch}/auto/Wx
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.980.0-2
+ Revision: 773653
- clean out spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.980.0-1mdv2011.0
+ Revision: 572267
- update to 0.98

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.200-3mdv2011.0
+ Revision: 556370
- change min version in buildrequires
- add minimum version in buildrequires:
- rebuild for perl 5.12
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.200-1mdv2011.0
+ Revision: 552496
- update to 0.9702

* Fri Apr 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.100-2mdv2010.1
+ Revision: 538298
- adding missing provides:

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.100-1mdv2010.1
+ Revision: 504496
- update to 0.9701

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.0-1mdv2010.1
+ Revision: 503737
- update to 0.97

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.1
+ Revision: 488854
- update to 0.96

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.950.0-1mdv2010.1
+ Revision: 483880
- update to 0.95

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.1
+ Revision: 463145
- update to 0.94

* Fri Sep 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.0
+ Revision: 448609
- update to 0.93

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 415113
- update to 0.92

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 408101
- rebuild using %%perl_convert_version

* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-3mdv2010.0
+ Revision: 399635
- rebuild with fixed perl-Alien-wxWidgets package (fix #45256)

* Wed Jun 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91-2mdv2010.0
+ Revision: 386781
- adding missing provides:

* Mon May 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2010.0
+ Revision: 376915
- update to new version 0.91

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90-1mdv2010.0
+ Revision: 374344
- update to new version 0.90

* Sat May 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.89-4mdv2010.0
+ Revision: 373698
- forcing rebuild

* Sun Feb 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.89-3mdv2009.1
+ Revision: 340471
- removing non-unicode dependency

* Sat Feb 14 2009 Olivier Thauvin <nanardon@mandriva.org> 0.89-2mdv2009.1
+ Revision: 340292
- fix buildrequires

  + Jérôme Quelin <jquelin@mandriva.org>
    - fix bug #47728: part two

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.89-1mdv2009.1
+ Revision: 311972
- update to new version 0.89

* Mon Nov 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.88-1mdv2009.1
+ Revision: 301684
- update to new version 0.88

* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.87-1mdv2009.1
+ Revision: 301381
- update to new version 0.87

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdv2009.0
+ Revision: 281120
- update to new version 0.86

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.85-1mdv2009.0
+ Revision: 278093
- Add sources
- New version 0.85

* Sat Aug 23 2008 Olivier Thauvin <nanardon@mandriva.org> 0.84-2mdv2009.0
+ Revision: 275366
- fix #43053

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2009.0
+ Revision: 230284
- update to new version 0.84

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2009.0
+ Revision: 209845
- new version

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-1mdv2009.0
+ Revision: 193956
- update to new version 0.82

* Sun Feb 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2008.1
+ Revision: 164876
- new version

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.27-2mdv2008.1
+ Revision: 152411
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.27-1mdv2008.1
+ Revision: 123985
- kill re-definition of %%buildroot on Pixel's request


* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdk
- New release 0.27
- spec cleanup
- fix directory ownership

* Thu Dec 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.26-1mdk
- 0.26
- Require most recent wxGTK

* Thu Sep 29 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.25-1mdk
- 0.25

* Fri Mar 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.22-1mdk
- first mdk release (by trem, <trem@zarb.org>)

