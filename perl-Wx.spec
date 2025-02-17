%define upstream_name Wx
%define upstream_version 0.9928

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Interface to the wxWidgets GUI toolkit

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc

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
Provides:	perl(Wx::InfoBar)
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
Provides:	perl(Wx::PlHeaderCtrl)
Provides:	perl(Wx::PlHeaderCtrlSimple)
Provides:	perl(Wx::PlHVScrolledWindow)
Provides:	perl(Wx::PlLog)
Provides:	perl(Wx::PlLogPassThrough)
Provides:	perl(Wx::PlPopupTransientWindow)
Provides:	perl(Wx::PlSizer)
Provides:	perl(Wx::PlThreadEvent)
Provides:	perl(Wx::PlTreeListItemComparator)
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
Provides:	perl(Wx::PropertyGrid)
Provides:	perl(Wx::RadioBox)
Provides:	perl(Wx::RadioButton)
Provides:	perl(Wx::RearrangeCtrl)
Provides:	perl(Wx::Rect)
Provides:	perl(Wx::RegConfig)
Provides:	perl(Wx::Region)
Provides:	perl(Wx::Ribbon)
Provides:	perl(Wx::RibbonBar)
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
Provides:	perl(Wx::TreeListCtrl)
Provides:	perl(Wx::UpdateUIEvent)
Provides:	perl(Wx::URLDataObject)
Provides:	perl(Wx::Validator)
Provides:	perl(Wx::View)
Provides:	perl(Wx::Wave)
Provides:	perl(Wx::WebView)
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
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README.txt
%{perl_vendorarch}/Wx.pm
%{perl_vendorarch}/Wx
%{perl_vendorarch}/auto/Wx
%doc %{_mandir}/*/*
%{_bindir}/*



